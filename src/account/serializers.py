from rest_framework import serializers
from account import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupChoice
        fields = ('choice', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, slug_field="choice", queryset=models.GroupChoice.objects.all())

    class Meta:
        model = models.Profile
        fields = ('id', 'join_date', 'user', 'nick', 'motivation', 'signed', 'groups')

    def validate(self, data):
        if data['join_date'] > models.Deadline.get_solo().deadline:
            raise serializers.ValidationError("join_date more than deadline")
        return data
