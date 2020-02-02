from rest_framework import routers
from mentors import views


router = routers.DefaultRouter()
router.register(r'mentors', views.MentorssViewSet, base_name='mentors')

urlpatterns = router.urls
