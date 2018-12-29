from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault
from . import models


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ('created_at', 'update_at', 'created_by')


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Note
        fields = '__all__'
        read_only_fields = ('created_at', 'update_at', 'created_by')
