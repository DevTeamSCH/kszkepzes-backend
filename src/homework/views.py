from rest_framework import viewsets

from common import permissions
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )


class SolutionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        queryset = models.Solution.objects.filter(created_by=user.profile)
        if user.has_perm(permissions.IsStaffUser):
            queryset = models.Solution.objects.all()
            profile_id = self.request.query_params.get('profileID', None)
            if profile_id is not None:
                queryset = queryset.filter(created_by=profile_id)
        return queryset
