from rest_framework import serializers
from django.utils import timezone
from account.models import Profile
from . import models
from common import email
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

    def create(self, validated_data):
        emails = Profile.objects.filter(role="Student").exclude(user__email='').values_list('user__email', flat=True)
        email.new_homework(emails)
        return self.Meta.model.objects.create(**validated_data)


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

    def validate_task(self, value):
        if timezone.now() > value.deadline:
            raise serializers.ValidationError('You late.')
        return value

    def validate(self, data):
        profile = CurrentUserMiddleware.get_current_user_profile()
        if profile.role != 'Staff' and (data['accepted'] or data['corrected'] or data['note'] != ''):
            raise serializers.ValidationError("You don't have permission!")
        return data

    def update(self, instance, validated_data):
        if instance.corrected == False and validated_data.get('corrected', instance.corrected) == True:
            email.homework_corrected(instance.created_by.user.email)
        return super().update(instance, validated_data)
