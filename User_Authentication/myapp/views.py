import logging
from .serializers import *
from django.conf import settings
from django.db import transaction
from .email_function import email_func
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsStaffOrAdminUser, IsAdminUser
from django.utils.http import urlsafe_base64_decode, base36_to_int
from django.contrib.auth.tokens import PasswordResetTokenGenerator

logger = logging.getLogger("Users")

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        logger.info(f"New user registered: {user.email}")
        return Response({"email": user.email, "message": "Users registered successfully"}, status=status.HTTP_201_CREATED,)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDeatilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return self.request.user

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            logger.warning(f"Failed login attempt: {request.data.get('email')} - {str(e)}")
            raise
        user = serializer.validated_data
        token = get_tokens_for_user(user)
        logger.info(f"User logged in: {user.email}")
        return Response({"Message": "Login Successful", "token": token}, status=status.HTTP_200_OK)

class LogoutView(generics.CreateAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsStaffOrAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User logged out successfully.")
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Logout failed: {str(e)}")
            return Response({"error": f"Logout failed: {e}"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.CreateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            if not check_password(old_password, user.password):
                logger.warning(f"Password change failed for {user.email}: incorrect old password")
                return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_password:
                logger.warning(f"Password change failed for {user.email}: password mismatch")
                return Response({"error": "New passwords and Confirm Passwords do not match.."}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            logger.info(f"Password changed successfully for user: {user.email}")
            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)

        logger.error(f"Password change validation error for {user.email}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordRequestView(generics.CreateAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            email_body, plain_message = email_func(user)
            msg = EmailMultiAlternatives(
                subject="Password Reset Request",
                body=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email]
            )
            msg.attach_alternative(email_body, "text/html")
            msg.send()
            logger.info(f"Password reset email sent to {email}")
        else:
            logger.warning(f"Password reset requested for non-existent email: {email}")

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"detail": "We’ve sent a password reset link to your email address."},
                        status=status.HTTP_200_OK)

class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def check_token_with_reason(self, user, token):
        if not (user and token):
            return False, "invalid"

        # Split token
        try:
            ts_b36, _ = token.split("-")
            ts = base36_to_int(ts_b36)
        except Exception:
            return False, "invalid"

        # Expiry check
        timeout = getattr(settings, "PASSWORD_RESET_TIMEOUT", 60 * 30)  # default 1hr
        if (self._num_seconds(self._now()) - ts) > timeout:
            return False, "expired"

        # Standard check
        if not super().check_token(user, token):
            return False, "used"

        return True, "valid"

account_activation_token = CustomPasswordResetTokenGenerator()

class PasswordResetConfirmView(generics.UpdateAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        uidb64, token = kwargs.get("uidb64"), kwargs.get("token")
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        valid, reason = account_activation_token.check_token_with_reason(user, token)

        if valid and user:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user.set_password(serializer.validated_data['new_password'])
                user.save(update_fields=["password"])

            logger.info(f"Password reset successful for user_email={user.email}")
            return Response({"detail": "Your password has been reset successfully."}, status=status.HTTP_200_OK,)

        error_messages = {"expired": "Your reset link has expired. Please request a new one.",
                          "used": "This reset link has already been used. Request a fresh link.",
                          "invalid": "Invalid reset link. Please double-check or request again.",}

        message = error_messages.get(reason, "Invalid reset attempt.")

        logger.warning(f"Password reset failed: reason={reason}, uidb64={uidb64}")
        return Response({"detail": message}, status=status.HTTP_400_BAD_REQUEST)
