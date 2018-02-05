from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksViewSet, base_name='tasks')
router.register(r'solutions', views.SolutionsViewSet, base_name='solutions')

urlpatterns = router.urls
