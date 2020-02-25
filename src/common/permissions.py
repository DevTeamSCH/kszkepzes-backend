from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or\
            (request.user.is_authenticated and request.user.profile.role == 'Staff')


class IsStaffOrReadOnlyForAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and\
            (request.method in SAFE_METHODS or request.user.profile.role == 'Staff')


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.profile.role == 'Staff'


class IsSafeOrPatch(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.method == 'PATCH'


class IsStaffOrStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and\
            (request.user.profile.role ==
             'Staff' or request.user.profile.role == 'Student')
