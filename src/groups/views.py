from rest_framework import viewsets

from . import serializers
from . import models

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    