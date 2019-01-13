from rest_framework import serializers

from common.serializers import CurrentUserProfileDefault
from . import models


class DocumentSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=CurrentUserProfileDefault())
    uploaded_by_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Document
        fields = ('uploaded_by', 'uploaded_at', 'name', 'description', 'file', 'uploaded_by_name', 'solution', )

    def get_uploaded_by_name(self, obj):
        return obj.uploaded_by.full_name
