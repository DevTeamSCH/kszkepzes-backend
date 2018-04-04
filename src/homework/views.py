from rest_framework import viewsets, status
from rest_framework.response import Response

from common import permissions
from . import serializers
from . import models


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )


class SolutionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )
