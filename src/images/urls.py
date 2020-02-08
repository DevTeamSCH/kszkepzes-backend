from rest_framework import routers
from images import views


router = routers.DefaultRouter()
router.register(r'images', views.ImagesViewSet, base_name='images')

urlpatterns = router.urls
