from django.conf.urls import url

from . import views

app_name = 'nori'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^created/$', views.created, name='created'),
    url(r'^(?P<nori_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<nori_id>[0-9]+)/send/$', views.send, name='send'),
]
