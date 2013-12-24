from django.conf.urls import patterns, url
from timeline import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^create/$', views.create, name='create'),
    url(r'^list/(?P<timeLineId>\w+)$', views.list, name='list'),
)

