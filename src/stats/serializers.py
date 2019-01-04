from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault
from . import models


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    created_by_name = serializers.SerializerMethodField()
    visitor_number = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = '__all__'
        read_only_fields = ('created_at', 'update_at', 'created_by')

    def get_created_by_name(self, obj):
        return obj.created_by.full_name

    def get_visitor_number(self, obj):
        return obj.visitors.all().count()


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Note
        fields = '__all__'
        read_only_fields = ('created_at', 'update_at', 'created_by')

    def get_creted_by_name(self, obj):
        return obj.created_by.full_name
