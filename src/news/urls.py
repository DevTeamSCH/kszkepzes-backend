from rest_framework import routers
from news import views


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'news', views.NewsViewSet)

urlpatterns = router.urls
