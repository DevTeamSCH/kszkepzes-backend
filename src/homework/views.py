from rest_framework import viewsets

from . import serializers
from . import models


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class SolutionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
