from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'monitor.views.home', name='home'),
	url(r'^alert/$', 'monitor.views.alert', name='alert'),
)
