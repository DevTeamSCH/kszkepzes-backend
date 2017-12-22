from rest_framework import routers
from django.conf.urls import url
from news.views import NewsListView, NewsDetailView, NewsUpdateView

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^news/$', NewsListView.as_view()),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailView.as_view()),
    url(r'^news/edit/(?P<pk>\d+)/$', NewsUpdateView.as_view()),
]

urlpatterns += router.urls
