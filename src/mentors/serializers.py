from mentors.models import Mentor
from rest_framework import serializers


class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = '__all__'

    def to_representation(self, instance):
        response = super(
            MentorSerializer,
            self
        ).to_representation(instance)
        if instance.image:
            response['image'] = instance.image.url
        return response
