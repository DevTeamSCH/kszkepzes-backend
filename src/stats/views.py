from rest_framework import viewsets
from . import models
from . import serializers
from common.permissions import IsStaffUser, IsStaffOrReadOnlyForAuthenticated


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    permission_classes = (IsStaffOrReadOnlyForAuthenticated, )


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    permission_classes = (IsStaffUser, )
