from common.permissions import IsStaffOrStudent, \
    IsStaffOrReadOnlyForAuthenticated
from rest_framework import viewsets
from images.models import Images
from images.serializers import ImagesSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ImagesSerializer
    permission_classes = (
        IsStaffOrReadOnlyForAuthenticated,
        IsStaffOrStudent,
    )
    queryset = Images.objects.all()
