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
        queryset = models.Solution.objects.filter(created_by=user)
        if user.has_perm(permissions.IsStaffUser):
            queryset = models.Solution.objects.all()
            user_id = self.request.query_params.get('userID', None)
            if user_id is not None:
                queryset = queryset.filter(created_by=user_id)
        return queryset
