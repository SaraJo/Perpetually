import gdata.service
import gdata.analytics
import gdata.analytics.service
import urllib
from django import http
from django import shortcuts
from django.shortcuts import render_to_response

default_host = 'https://www.google.com'
user_agent = 'python-gapi-1.0'
auth_token = None

def authorize(request):
    next = 'http://localhost:8000/authconfirm'
    scope = 'https://www.google.com/analytics/feeds'
    secure = True  # set secure=True to request secure AuthSub tokens
    session = True
    auth_sub_url = gdata.service.GenerateAuthSubRequestUrl(next, scope, secure=secure, session=session)
    return http.HttpResponseRedirect(auth_sub_url)

def index(request):
    return render_to_response('index.html')


def auth_confirm(request):   
    feedUri='https://www.google.com/analytics/feeds/accounts/default?max-results=50'
    service = gdata.analytics.service.AccountsService()
    feed = service.QueryAccountListFeed(feedUri)
    #for entry in feed.entry:
    #    text = text + entry['ga:accountName'] + "m"
    #return http.HttpResponse(str(feed))
    return render_to_response('TestData.html', {'random_value' : text} )
