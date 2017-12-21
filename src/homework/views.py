from rest_framework import viewsets


from . import serializers
from . import models
from . import permissions


class TasksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (permissions.IsStaffOrReadOnly,)


class SolutionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SolutionSerializer
    queryset = models.Solution.objects.all()
    #permission_classes = ()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

