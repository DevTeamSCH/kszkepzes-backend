from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route
from django.http import Http404
from django.shortcuts import get_object_or_404
import datetime
from django.utils.timezone import utc

from . import serializers
from . import models
from . import permissions


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )


class SolutionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )

    def perform_create(self, serializer):
        serializer.validated_data['accepted'] = False
        task = serializer.validated_data['task']
        # task = get_object_or_404(models.Task, pk=task_id.id)
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        if task.deadline < now:
            raise Http404("Deadline")
        serializer.save()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.has_perm(permissions.IsStaffUser):
    #         return models.Solution.objects.all()
    #
    # @list_route(methods=['get'])
    # def me(self, request):
    #     serializer = self.serializer_class(request.user.profile) #request ?
    #     return Response(serializer.data)