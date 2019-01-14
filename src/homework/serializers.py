from rest_framework import serializers
from django.utils import timezone

from common.serializers import CurrentUserProfileDefault
from . import models
from common.middleware import CurrentUserMiddleware


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        read_only_fields = ('created_by', 'created_at', 'updated_at')
        fields = '__all__'

    def validate(self, data):
        if timezone.now() >= data['deadline']:
            raise serializers.ValidationError('Please, enter appropriate deadline.')
        return data


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solution
        read_only_fields = ('created_by', 'created_at', 'updated_at', 'ready', 'files')
        fields = (
            'task',
            'created_at',
            'updated_at',
            'accepted',
            'files',
            'created_by',
            'corrected',
            'note',
        )

    def validate(self, data):
        if timezone.now() > data['task'].deadline:
            raise serializers.ValidationError('You late.')
        profile = CurrentUserMiddleware.get_current_user_profile()
        if profile.role != 'Staff' and (data['accepted'] or data['corrected'] or data['note'] != ''):
            raise serializers.ValidationError("You don't have permission!")
        return data
