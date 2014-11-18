from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from desk import urls as deskURL
from login import urls as loginURL
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webdesk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include(loginURL)),
    url(r'^desk/', include(deskURL)),
    url(r'^$', renderIndex),
)
