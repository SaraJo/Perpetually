from django.conf.urls.defaults import *
from google_analytics import login
from top_urls import url_parse
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', login.authorize),
    url(r'^authconfirm$', login.auth_confirm),
    url(r'^index$', login.index),
    url(r'^scrape$', url_parse.get_parse_list)
)
