from rest_framework import serializers
from account import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupChoice
        fields = ('choice', )


class ProfileSerializer(serializers.ModelSerializer):
    preferd_groups = serializers.SlugRelatedField(slug_field='choice', many=True, queryset=models.GroupChoice.objects.all())

    class Meta:
        model = models.Profile
        fields = ('join_date', 'user', 'nick', 'signed', 'preferd_groups')
