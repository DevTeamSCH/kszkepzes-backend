from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'profiles', views.ProfileViewSet, base_name='profile')
urlpatterns = router.urls
