from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'staff_events', views.StaffEventViewSet, base_name='staff_events')
router.register(r'student_events', views.StudentEventViewSet, base_name='student_events')
router.register(r'notes', views.NoteViewSet, base_name='notes')

urlpatterns = router.urls
