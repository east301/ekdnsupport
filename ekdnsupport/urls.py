from django.conf.urls import patterns, include, url
from . import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ekdnsupport.views.home', name='home'),
    # url(r'^ekdnsupport/', include('ekdnsupport.foo.urls')),
)

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
