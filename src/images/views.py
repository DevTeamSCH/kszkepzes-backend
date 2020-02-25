from common.permissions import IsStaffOrReadOnly
from rest_framework import viewsets
from images.models import Image
from images.serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = (IsStaffOrReadOnly, )
    queryset = Image.objects.all()
