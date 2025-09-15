from rest_framework.permissions import *



class IsStaffOrAdminUser(BasePermission):
    def has_permission(self, request, view):
        is_staff_user = bool(request.user and request.user.is_authenticated and request.user.is_staff)
        is_admin_user = bool(request.user and request.user.is_authenticated and request.user.is_admin)
        return is_staff_user or is_admin_user

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin)

class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
