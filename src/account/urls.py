from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'profiles', views.ProfileViewSet)
urlpatterns = [
        url(r'^profiles/create', views.ProfileCreateView.as_view()),
        url(r'^profiles/update/<pk>', views.ProfileUpdateView.as_view())
]
urlpatterns += router.urls
