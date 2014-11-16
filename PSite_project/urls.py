from django.conf.urls import patterns, include, url
from django.conf import settings
from PSite_project import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portafolio/',include('portafolio.urls', namespace="portafolio")),
    url(r'^blog/',include('blog.urls')),
    url(r'^rango/',include('rango.urls')),
    url(r'^$',views.index,name='index'),
)


# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
