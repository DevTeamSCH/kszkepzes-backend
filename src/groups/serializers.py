from rest_framework import serializers
from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        read_only_fields = (
            'name',
            'description',)
        fields = (
            'name',
            'description',
        )


