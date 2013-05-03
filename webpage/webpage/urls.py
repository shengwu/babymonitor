from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('monitor.urls', namespace='monitor')),
	url(r'^register', 'webpage.views.register', name='register'),
    url(r'^owner', 'webpage.views.register_owner', name='register_owner'),
	url(r'^login/', 'webpage.views.login_view', name='login_view'),
	url(r'^logout/', 'webpage.views.logout_view', name='logout_view'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url("", include("django_socketio.urls")),
)
