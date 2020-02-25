from images.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

    def to_representation(self, instance):
        response = super(
            ImageSerializer,
            self
        ).to_representation(instance)
        if instance.image:
            response['image'] = instance.image.url
        return response
