from rest_framework import serializers
from . import models


class KszkEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KszkEvent
        fields = ('date',  'visitors')
