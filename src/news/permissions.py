from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS
