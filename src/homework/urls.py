from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksViewSet)
router.register(r'solutions', views.SolutionViewSet)

urlpatterns = router.urls
