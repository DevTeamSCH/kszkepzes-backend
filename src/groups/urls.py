from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'groups', views.GroupsViewSet, base_name='groups')
urlpatterns = router.urls
