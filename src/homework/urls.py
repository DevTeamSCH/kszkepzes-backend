from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'students', views.StudentViewSet)

app_name = 'homework'
urlpatterns = router.urls
