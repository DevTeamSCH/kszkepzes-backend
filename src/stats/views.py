from rest_framework import viewsets

from . import models
from . import serializers


class KszkEventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.KszkEventSerializer
    queryset = models.KszkEvent.objects.all()
