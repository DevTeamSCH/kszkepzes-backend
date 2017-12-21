from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = ('created_by', 'date')
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solution
        fields = '__all__'
        read_only_fields = ('created_by', 'date')
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
