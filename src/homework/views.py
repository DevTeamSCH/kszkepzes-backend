from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route
from django.http import Http404
from django.shortcuts import get_object_or_404

from . import serializers
from . import models
from base import permissions


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )


class SolutionsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnlyForAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data['accepted'] = False
        # task_id = serializer.validated_data.get('task')
        # date = serializer.validated_data['date']
        # task = get_object_or_404(models.Task, pk=task_id)
        # if task_id.deadline < date:
        #     return Http404("Deadline")
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user = self.request.user
        if user.has_perm(permissions.IsStaffUser):
            return models.Solution.objects.all()

    @list_route(methods=['get'])
    def me(self, request):
        serializer = self.serializer_class(request.user.profile) #request ?
        return Response(serializer.data)