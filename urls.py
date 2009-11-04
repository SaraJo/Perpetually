from django.conf.urls.defaults import *
from google_analytics import login
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', login.authorize),
    url(r'^authconfirm$', login.auth_confirm),
    url(r'^index$', login.index)
)
