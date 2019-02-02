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
        profiles = Profile.objects.filter(role="Student").exclude(user__email='')
        for profile in profiles:
            email.new_homework(profile.user, validated_data.get('deadline'))
        return self.Meta.model.objects.create(**validated_data)


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solution
        read_only_fields = ('created_by', 'created_at', 'updated_at', 'ready', 'files')
        fields = (
            'id',
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

    def validate_accepted(self, value):
        profile = CurrentUserMiddleware.get_current_user_profile()
        if profile.role != 'Staff' and value:
            raise serializers.ValidationError("You don't have permission to modify accepted!")
        return value

    def validate_corrected(self, value):
        profile = CurrentUserMiddleware.get_current_user_profile()
        if profile.role != 'Staff' and value:
            raise serializers.ValidationError("You don't have permission to modify corrected!")
        return value

    def validate_note(self, value):
        profile = CurrentUserMiddleware.get_current_user_profile()
        if profile.role != 'Staff' and value != '':
            raise serializers.ValidationError("You don't have permission to create note!")
        return value

    def update(self, instance, validated_data):
        if instance.corrected is not True and validated_data.get('corrected', instance.corrected) is True:
            email.homework_corrected(
                instance.created_by.user,
                instance.task.title,
                validated_data.get('accepted', instance.accepted)
            )
        return super().update(instance, validated_data)

    def create(self, validated_data):
        profile = CurrentUserMiddleware.get_current_user_profile()
        models.Solution.objects.filter(created_by=profile, task=validated_data['task']).delete()
        return super().create(validated_data)
