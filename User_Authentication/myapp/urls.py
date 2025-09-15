from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (RegisterView, UserListView, UserDeatilView, MeView, LoginView, LogoutView, ChangePasswordView,
                    ResetPasswordRequestView, PasswordResetConfirmView)


urlpatterns = [
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path('register/', RegisterView.as_view(), name='register'),
                path('ls/', UserListView.as_view(), name='user-list'),
                path('detail/<int:pk>/', UserDeatilView.as_view(), name='user-detail'),
                path('me/', MeView.as_view(), name='me'),

                path('login/', LoginView.as_view(), name='login'),
                path('logout/', LogoutView.as_view(), name='logout'),

                path('pw/change/', ChangePasswordView.as_view(), name='change_password'),
                path('pw/reset/', ResetPasswordRequestView.as_view(), name='password_reset'),
                path('pw/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        ]
