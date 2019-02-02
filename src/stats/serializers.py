from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault
from . import models


class StaffEventSerializer(serializers.ModelSerializer):
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

    def validate(self, data):
        if 'absent' in data and 'visitors' in data:
            for i in data['absent']:
                if i in data['visitors']:
                    raise serializers.ValidationError('You cant add a student to absent and visitor in the same time.')
        return data


class StudentEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id', 'name', 'date', 'description', )
        read_only_fields = ('id', 'name', 'date', 'description', )


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Note
        fields = '__all__'
        read_only_fields = ('created_at', 'update_at', 'created_by')

    def get_created_by_name(self, obj):
        return obj.created_by.full_name

    def validate(self, data):
        if data['profile'] is None and data['event'] is None:
            raise serializers.ValidationError('You have to add profile or event')
        return data
