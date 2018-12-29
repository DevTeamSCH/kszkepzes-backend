from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'documents', views.DocumentViewSet, base_name='documents')

urlpatterns = router.urls
