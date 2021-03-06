from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^chat/', include('chat.urls')), 
    url(r'^iot/', include('iot.urls')),
    url(r'^translate/', include('translate.urls')),
    url(r'^three/', include('three.urls')),
    url(r'^vr/', include('vr.urls')),
    # Examples:
    # url(r'^$', 'Servicize2.views.home', name='home'),
    # url(r'^Servicize2/', include('Servicize2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'serve'),
)

# Add static root
# urlpatterns += staticfiles_urlpatterns()
