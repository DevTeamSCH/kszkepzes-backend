from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('social_django.urls', namespace='social')),
    url(r'^api/v1/homework/', include('homework.urls')),
    url(r'^api/v1/', include('stats.urls')),
    url(r'^api/v1/', include('account.urls')),
    url(r'^api/v1/', include('news.urls')),

    url(r'^api/v1/logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
