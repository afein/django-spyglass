from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import landing
from core.views import thanks
from core.views import profile
import spyglass.urls

import allauth.urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', landing),
    url(r'^thanks/$', thanks.as_view(), name="thanks"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(spyglass.urls)),
    url(r'^accounts/', include(allauth.urls)),
    url(r'^accounts/profile/', profile, name="profile"),
)
