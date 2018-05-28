from rest_framework import serializers

from common.serializers import CurrentUserProfileDefault
from . import models


class DocumentSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(read_only=True)
    uploaded_by = serializers.HiddenField(default=CurrentUserProfileDefault())

    class Meta:
        model = models.Document
        fields = ('uploaded_by', 'uploaded_at', 'name', 'description', 'file')
