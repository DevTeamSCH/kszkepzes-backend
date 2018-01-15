from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProfileCreateSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated, ]


class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.ProfileDetailSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated, ]


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ProfileUpdateSerializer
    queryset = models.Profile.objects.all()
    permission_classes = [IsAuthenticated, ]


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = models.Profile.objects.all()
