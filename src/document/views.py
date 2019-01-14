from rest_framework import viewsets

from common import permissions
from . import models
from . import serializers


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = (permissions.IsStaffOrStudent, )
