from mentors.models import Mentor
from rest_framework import serializers
from common.serializers import CurrentUserProfileDefault


class MentorSerializer(serializers.ModelSerializer):
    mentor = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        read_only_fields = ('mentor', )
        fields = '__all__'

    def get_mentor(self, obj):
        return obj.mentor.full_name
