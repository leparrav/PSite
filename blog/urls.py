from django.conf.urls import url
from blog             import views

urlpatterns = [
	url(r'(?P<post_page>^$)',views.index,name='index'),
	url(r'(?P<post_page>^\d+)',views.index,name='index'),
	url(r'^post/(?P<post_pk>\d+)',views.post,name='post'),
	url(r'^search/$', views.search, name='search'),
    url(r'^search_suggest/$', views.search_suggest, name='search_suggest'),
	]