from common.permissions import IsStaffOrStudent
from rest_framework import viewsets
from mentors.models import Mentor
from mentors.serializers import MentorSerializer


class MentorssViewSet(viewsets.ModelViewSet):
    serializer_class = MentorSerializer
    permission_classes = (IsStaffOrStudent,)
    queryset = Mentor.objects.all().order_by('name')
