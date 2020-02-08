from common.permissions import IsStaffOrStudent, \
    IsStaffOrReadOnlyForAuthenticated
from rest_framework import viewsets
from mentors.models import Mentor
from mentors.serializers import MentorSerializer


class MentorsViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSerializer
    permission_classes = (
        IsStaffOrReadOnlyForAuthenticated,
        IsStaffOrStudent,
    )
    queryset = Mentor.objects.all().order_by('name')

    def perform_create(self, serializer):
        kwargs = {
            'mentor': self.request.user.profile
        }
 
        serializer.save(**kwargs)