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
    permission_classes = (IsStaffUser, )

    def get_queryset(self):
        queryset = models.Note.objects.all()
        profile_id = self.request.query_params.get('profileID', None)
        event_id = self.request.query_params.get('eventID', None)
        if profile_id is not None and event_id is not None:
            return queryset.filter(user=profile_id, event=event_id)
        if profile_id is not None:
            return queryset.filter(user=profile_id)
        if event_id is not None:
            return queryset.filter(event=event_id)
        return queryset
