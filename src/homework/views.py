from rest_framework import viewsets

from . import serializers
from . import models
from common import permissions


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, permissions.IsStaffOrStudent, )

class SolutionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer_Student
    permission_classes = (permissions.IsStaffOrStudent, )

    def get_serializer_class(self):
        user = self.request.user
        if user.profile.role == 'Staff':
            return serializers.SolutionSerializer_Staff
        return serializers.SolutionSerializer_Student

    def get_queryset(self):
        user = self.request.user
        queryset = models.Solution.objects.filter(created_by=user.profile)
        if user.profile.role == 'Staff':
            queryset = models.Solution.objects.all()
            profile_id = self.request.query_params.get('profileID', None)
            if profile_id is not None:
                queryset = queryset.filter(created_by=profile_id)
        return queryset
