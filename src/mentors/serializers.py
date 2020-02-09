from mentors.models import Mentor
from rest_framework import serializers


class MentorSerializer(serializers.ModelSerializer):
    mentor = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        read_only_fields = ('mentor', )
        fields = '__all__'

    def get_mentor(self, obj):
        return obj.mentor.full_name
    
    def to_representation(self, instance):
        response = super(
            MentorSerializer,
            self
        ).to_representation(instance)
        if instance.image:
            response['image'] = instance.image.url
        return response
