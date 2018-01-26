from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadOnlyForAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS and request.user.is_authenticated
