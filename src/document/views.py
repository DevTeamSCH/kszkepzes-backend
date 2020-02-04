from rest_framework import viewsets
from common import permissions
from . import models
from . import serializers
from rest_framework.parsers import JSONParser, MultiPartParser
from django.http import HttpResponse, Http404
from rest_framework.decorators import action
import os

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DocumentSerializer
    permission_classes = (permissions.IsStaffOrStudent, )
    parser_classes = (JSONParser, MultiPartParser)

    def get_queryset(self):
        user = self.request.user
        if user.profile.role == 'Staff':
            queryset = self.staff_queryset()
        else:
            queryset = self.student_queryset(user.profile)
        return queryset

    def staff_queryset(self):
        queryset = models.Document.objects.all()
        profile_id = self.request.query_params.get('profileID', None)
        solution_id = self.request.query_params.get('solutionID', None)
        if profile_id is not None and solution_id is not None:
            return queryset.filter(uploaded_by=profile_id, solution=solution_id)
        if profile_id is not None:
            return queryset.filter(uploaded_by=profile_id)
        if solution_id is not None:
            return queryset.filter(solution=solution_id)
        return queryset

    def student_queryset(self, profile):
        queryset = models.Document.objects.filter(uploaded_by=profile)
        solution_id = self.request.query_params.get('solutionID', None)
        if solution_id is not None:
            return queryset.filter(solution=solution_id)
        return queryset
    
    def perform_create(self, serializer):
        kwargs = {
            'uploaded_by': self.request.user.profile
        }
 
        serializer.save(**kwargs)

    @action(detail=True, methods=["get"])
    def download(self, request, pk):
        document = self.get_object()
        with document.file.open() as fh:
            response = HttpResponse(fh.read(), content_type="application/media")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(document.file.name)
            return response
        raise Http404
