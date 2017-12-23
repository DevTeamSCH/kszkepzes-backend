from rest_framework import serializers
from . import models


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = [
                'user.username',
                'nick',
                'pref_group',
                'signed',
                  ]

    # def create(self, *args, **kwargs, obj):
