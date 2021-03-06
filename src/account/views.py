from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route
from common.permissions import IsSafeOrPatch

from . import models
from . import serializers


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsSafeOrPatch)

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == 'Staff':
            role = self.request.query_params.get("role", None)
            if role is not None:
                return models.Profile.objects.filter(role=role)
            return models.Profile.objects.all()
        return models.Profile.objects.filter(pk=user.profile.id)

    @list_route(methods=['get'])
    def me(self, request):
        serializer = self.serializer_class(request.user.profile)
        return Response(serializer.data)
