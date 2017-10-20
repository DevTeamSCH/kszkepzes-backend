from rest_framework import serializers
from . import models


class KszkEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KszkEvent
        fields = ('date', 'num_of_pers', 'visitors')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
