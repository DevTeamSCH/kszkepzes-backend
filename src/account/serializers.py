from rest_framework import serializers
from account import models
from common.middleware import CurrentUserMiddleware


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupChoice
        fields = ('choice', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, slug_field='choice', queryset=models.GroupChoice.objects.all())
    updated_at = serializers.DateTimeField(read_only=True)
    signed = serializers.BooleanField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = (
            'id',
            'join_date',
            'updated_at',
            'nick',
            'signed',
            'groups',
            'motivation_about',
            'motivation_profession',
            'motivation_exercise',
            'full_name',
            'role',
        )

    def validate(self, data):
        deadline = models.Deadline.get_solo().deadline
        if data['signed'] is False:
            raise serializers.ValidationError("You cannot join without signed")
        if deadline is not None and data['updated_at'] > deadline:
            raise serializers.ValidationError("You cannot join after the deadline")
        modifier_role = CurrentUserMiddleware.get_current_user_profile().role
        role = data['role']
        if role is not None and modifier_role != 'Staff':
            raise serializers.ValidationError("You don't have permission to change role")
        return data

    def get_full_name(self, obj):
        return obj.full_name
