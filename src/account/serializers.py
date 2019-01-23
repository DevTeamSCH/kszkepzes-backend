from rest_framework import serializers
from account import models
from common.middleware import CurrentUserMiddleware
from common import email


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupChoice
        fields = ('choice', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(many=True, slug_field='choice', queryset=models.GroupChoice.objects.all())
    updated_at = serializers.DateTimeField(read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        read_only_fields = ('id', 'join_date', 'updated_at', 'full_name', )
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

    def validate_updated_at(self, value):
        deadline = models.Deadline.get_solo().deadline
        if deadline is not None and value > deadline:
            raise serializers.ValidationError("You cannot join after the deadline")
        return value

    def validate_role(self, value):
        modifier_role = CurrentUserMiddleware.get_current_user_profile().role
        if value != modifier_role and modifier_role != "Staff":
            raise serializers.ValidationError("You don't have permission change role")
        return value

    def validate_signed(self, value):
        modifier = CurrentUserMiddleware.get_current_user_profile()
        if value is False and modifier.role != "Staff":
            raise serializers.ValidationError("You cannot join without signed")
        return value

    def update(self, instance, validated_data):
        new_role = validated_data.get('role', instance.role)
        if instance.role != new_role:
            if new_role == 'Student':
                email.admitted(instance.user.email)
            if new_role == 'Denied':
                email.denied(instance.user.email)
        return super().update(instance, validated_data)

    def get_full_name(self, obj):
        return obj.full_name
