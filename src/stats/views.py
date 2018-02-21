from rest_framework import viewsets

from . import models
from . import serializers


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
