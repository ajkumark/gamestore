from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gameseller.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('authentication.urls')),
    url(r'^$', 'authentication.views.home', name='home'),
    url(r'^games/$', 'flashgames.views.games', name='games'),
    url(r'^admin/', include(admin.site.urls)),
)
