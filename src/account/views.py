from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from common.permissions import IsSafeOrPatch
from rest_framework_api_key.permissions import HasAPIKey

from . import models
from . import serializers


class MonitorinViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonitoringSerializer
    permission_classes = (HasAPIKey,)

    def get_queryset(self):
        return models.Profile.objects.filter(role='Student')


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer_User
    permission_classes = (permissions.IsAuthenticated, IsSafeOrPatch)

    def get_serializer_class(self):
        user = self.request.user
        if user.profile.role == 'Staff':
            return serializers.ProfileSerializer_Staff
        return serializers.ProfileSerializer_User

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == 'Staff':
            role = self.request.query_params.get("role", None)
            if role is not None:
                return models.Profile.objects.filter(role=role)
            return models.Profile.objects.all()
        return models.Profile.objects.filter(pk=user.profile.id)

    @action(detail=False)
    def me(self, request):
        serializer = self.serializer_class(request.user.profile)
        return Response(serializer.data)

    @action(detail=False)
    def deadline(self, request):
        deadline = models.Deadline.get_solo()
        return Response({
            'deadline': deadline.deadline,
            'messageBefore': deadline.messageBefore,
            'messageAfter': deadline.messageAfter
        })
