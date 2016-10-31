from django.conf.urls import include, url
from PSite_project    import views
from django.contrib   import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portafolio/',include('portafolio.urls', namespace="portafolio")),
    url(r'^blog/',include('blog.urls')),
    url(r'^rango/',include('rango.urls')),
    url(r'^$',views.index,name='index'),
]
