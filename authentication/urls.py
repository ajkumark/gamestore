from django.conf.urls import patterns, include, url


urlpatterns = patterns('authentication.views',
	url(r'^register/$', 'register', name='register'),
	url(r'^login/$', 'login', name='ulogin'),
	# url(r'^user/login/', name='login'),
	# url(r'^logout/$', 'user_logout', name='user_logout'),
)