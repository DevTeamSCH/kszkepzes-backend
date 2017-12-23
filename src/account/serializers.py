from rest_framework import serializers
from account.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    def current_user(self):
        user = self.context['request'].user
        return user

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Profile
        fields = [
                'first_name',
                'last_name',
                'email',
                'nick',
                'pref_group',
                'signed',
                  ]

    def create(self, validated_data):
        user = self.current_user()
        if User.objects.filter(username=user.get_username()) is None:
            user.first_name = validated_data['first_name']
            user.last_name = validated_data['last_name']
            user.email = validated_data['email']
            user.save()
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
        else:
            raise serializers.ValidationError("Már jelentkeztél, ha le akarsz jelentkezni hazsnáld a Lejelentkezés gombot!")
        return validated_data


class ProfileUpdateSerializer(serializers.ModelSerializer):
    def current_user(self):
        user = self.context['request'].user
        return user

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Profile
        fields = [
                'first_name',
                'last_name',
                'email',
                'nick',
                'pref_group',
                  ]

    def update(self, validated_data):
        user = self.current_user()
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.save()
        nick = validated_data['nick']
        pref_group = validated_data['pref_group']
        profile_obj = Profile(
                user=user,
                nick=nick,
                pref_group=pref_group,
                )
        profile_obj.save()
