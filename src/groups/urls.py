from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'group', views.GroupViewSet, base_name='group')
urlpatterns = router.urls
