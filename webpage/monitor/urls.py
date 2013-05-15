from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'monitor.views.home', name='home'),
	url(r'^alert/$', 'monitor.views.alert', name='alert'),
	url(r'^cries/$', 'monitor.views.cries', name='cries'),
	url(r'^users/$', 'monitor.views.users', name='users'),
	url(r'^modify_user/$', 'monitor.views.modify_user', name='modify_user'),
	url(r'^options/$', 'monitor.views.options', name='options'),
	url(r'^humiditytemp/$', 'monitor.views.get_humidity_and_temp', name='get_humidity_and_temp'),
    url(r'^create_baby/$', 'monitor.views.create_baby', name='create_baby'),
    url(r'^modify_baby/$', 'monitor.views.modify_baby', name='modify_baby'),
)
