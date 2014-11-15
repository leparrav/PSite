from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'(?P<post_page>^\d+)',views.index,name='index'),
	url(r'^post/(?P<post_pk>\d+)',views.post,name='post'),
	url(r'^search/$', views.search, name='search'),
    url(r'^search_suggest/$', views.search_suggest, name='search_suggest'),
	)