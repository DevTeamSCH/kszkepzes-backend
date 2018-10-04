from rest_framework import viewsets

from . import models
from . import serializers
from common.permissions import IsStaffUser

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    permission_classes = [IsStaffUser]