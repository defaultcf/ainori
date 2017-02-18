from django.conf.urls import url
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^login', login, {
        'template_name': 'myauth/login.html',
    }, name='login'),
    url(r'^logout', logout, name='logout'),
]
