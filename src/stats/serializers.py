from rest_framework import serializers
from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('date',  'visitors')
