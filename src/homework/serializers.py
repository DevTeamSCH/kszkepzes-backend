from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        read_only_fields = ('created_by', 'date')
        # extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Solution
        read_only_fields = ('created_by', 'date' 'ready')
        # extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        fields = ('task', 'date', 'accepted', 'files', 'created_by')

    # def validate(self, attrs):
    #     task = attrs['task']
    #     date = attrs['date'] keyerror
    #
    #     if task.deadline < date:
    #         raise serializers.ValidationError("You cannot submit homework after the deadline")
    #
    #     return attrs
