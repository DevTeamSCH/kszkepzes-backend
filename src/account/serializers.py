from rest_framework import serializers
from account.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    # Create a custom method field
    current_user = serializers.SerializerMethodField('_user')

    class Meta:
        model = Profile
        fields = [
                'current_user',
                'first_name',
                'last_name',
                'email',
                'nick',
                'pref_group',
                'signed',
                  ]

    def _user(self, obj):
        user = self.context['request'].user
        return user

    def create(self, validated_data):
        #user.first_name = validated_data['first_name']
        #user.last_name = validated_data['last_name']
        #user.email = validated_data['email']
        #user.save()
        nick = validated_data['nick']
        pref_group = validated_data['pref_group']
        signed = validated_data['signed']
        profile_obj = Profile(
                user=user,
                nick=nick,
                pref_group=pref_group,
                signed=signed,
        )
        profile_obj.save()
        return validated_data
