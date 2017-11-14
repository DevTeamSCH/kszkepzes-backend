from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'events', views.KszkEventViewSet)

# app_name = 'stats'
urlpatterns = router.urls
