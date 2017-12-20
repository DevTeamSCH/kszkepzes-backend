from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'events', views.KszkEventViewSet)

# app_name = 'stats'
urlpatterns = router.urls
