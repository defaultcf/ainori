from django.conf.urls import url, include
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^login/$', login, {
        'template_name': 'myauth/login.html',
    }, name='login'),
    url(r'^twitter', include('social_django.urls', namespace = 'social')),
    url(r'^logout/$', logout, name='logout'),
]
