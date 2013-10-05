from django.conf.urls import patterns, include, url
from . import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ekdnsupport.views.home', name='home'),
    # url(r'^ekdnsupport/', include('ekdnsupport.foo.urls')),

    url(r'^$', 'lib.views.home'),

    # django.contrib.auth
    url(r'^auth/login/$', 'django.contrib.auth.views.login', dict(template_name='auth/login.html')),
    url(r'^auth/logout/$', 'django.contrib.auth.views.logout', dict(next_page='/auth/login/')),

    # apps.mydata
    url(r'^mydata/upload/$', 'apps.mydata.views.upload'),
)

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
