from rest_framework import serializers

from common.serializers import CurrentUserProfileDefault
from . import models


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Task
        read_only_fields = ('created_by', 'date')
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Solution
        read_only_fields = ('created_by', 'date' 'ready')
        fields = ('task', 'date', 'accepted', 'files', 'created_by')
