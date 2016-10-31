from django.conf.urls import url
from portafolio       import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^courses/$',views.courses,name='courses'),
	url(r'^jobs/$',views.jobs,name='jobs'),
	url(r'^roadmap/$',views.roadmap,name="roadmap"),
	url(r'^projects/$',views.projects,name="projects"),
	]