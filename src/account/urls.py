from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'profiles', views.ProfileViewSet, base_name='profile')
router.register(r'monitoring/profiles', views.MonitorinViewSet, base_name='monitoring')

urlpatterns = router.urls
