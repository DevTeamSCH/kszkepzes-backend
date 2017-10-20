from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'events', views.KszkEventViewSet)
router.register(r'profiles', views.ProfileViewSet)


# app_name = 'stats'
urlpatterns = router.urls
