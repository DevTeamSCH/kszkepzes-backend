from rest_framework import serializers
from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        read_only_fields = (
            'id',
            'name',
            'description',)
        fields = (
            'id',
            'name',
            'description',
        )
