from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a staff, or is a read-only request.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_staff


class IsStaffOrReadOnlyForAuthenticated(BasePermission):
    """
    The request is authenticated as a staff, or is a read-only request for authenticated.
    """

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS and request.user.is_authenticated


class IsStaffUser(BasePermission):
    """
    The request is authenticated as a staff
    """

    def has_permission(self, request, view):
        return request.user.is_staff
