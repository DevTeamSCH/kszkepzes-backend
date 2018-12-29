from rest_framework import routers
from news import views


router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet, base_name='news')

urlpatterns = router.urls
