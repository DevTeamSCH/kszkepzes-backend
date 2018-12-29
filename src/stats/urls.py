from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet, base_name='events')
router.register(r'notes', views.NoteViewSet, base_name='notes')

urlpatterns = router.urls
