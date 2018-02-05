from rest_framework import serializers
from account import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupChoice
        fields = ('choice', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, slug_field="choice", queryset=models.GroupChoice.objects.all())
    updated_at = serializers.DateTimeField(read_only=True)
    signed = serializers.BooleanField()

    class Meta:
        model = models.Profile
        fields = (
            'id',
            'join_date',
            'updated_at',
            'user',
            'nick',
            'motivation',
            'signed',
            'groups',
            'motivation_about',
            'motivation_profession',
            'motivation_exercise',
        )

    def validate(self, data):
        deadline = models.Deadline.get_solo().deadline
        if deadline is None:
            return data

        if data['signed'] is True and data['updated_at'] > deadline:
            raise serializers.ValidationError("You cannot join after the deadline")

        return data
