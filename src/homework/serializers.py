from rest_framework import serializers
from django.utils import timezone

from common.serializers import CurrentUserProfileDefault
from . import models


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Task
        read_only_fields = ('created_by', 'created_at', 'updated_at')
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Solution
        read_only_fields = ('created_by', 'created_at', 'updated_at', 'ready')
        fields = ('task', 'created_at', 'updated_at', 'accepted', 'files', 'created_by')

    def validate(self, data):
        if timezone.now() > data['task'].deadline:
            raise serializers.ValidationError('You late.')
        return data
