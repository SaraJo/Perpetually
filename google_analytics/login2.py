import gdata.service
import gdata.analytics
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
    secure = False  # set secure=True to request secure AuthSub tokens
    session = False
    auth_sub_url = gdata.service.GenerateAuthSubRequestUrl(next, scope, secure=secure, session=session)
    return http.HttpResponseRedirect(auth_sub_url)

def index(request):
    return render_to_response('index.html')


def __init__(self, google_email=None, google_password=None):  
    authtoken_pat = re.compile(r"Auth=(.*)")
    path = '/accounts/ClientLogin'

    if google_email == None or google_password == None:
      google_email, google_password = config.get_google_credentials()
      
    data = "accountType=GOOGLE&Email=%s&Passwd=%s&service=analytics&source=%s"
    data = data % (google_email, google_password, self.user_agent)
    if DEBUG:
      print "Authenticating with %s / %s" % (google_email, google_password)
    response = self.make_request('POST', path=path, data=data)
    auth_token = authtoken_pat.search(response.read())
    self.auth_token = auth_token.groups(0)[0]


def auth_confirm(request):
    start_index=1
    max_results=None
    gdata_service = gdata.service.GDataService('iSample_acctSample_v1.0')
    data = { 'start-index': start_index }
    if max_results:
      data['max-results'] = 50
    feedUri='https://www.google.com/analytics/feeds/accounts/'
    # request feed
    #text = ""
    #feed = gdata.analytics.AnalyticsDataFeed(feedUri)
    #for entry in feed.entry:
    #    text = text + entry['ga:accountName'] + "m"
    #return http.HttpResponse(str(feed))
    data = urllib.urlencode(feedUri)
    response = self.make_request('GET', path, data=data)
    raw_xml = response.read()
    xml_tree = self.parse_response(raw_xml)
    account_list = []
    accounts = xml_tree.getiterator('{http://www.w3.org/2005/Atom}entry')
    for account in accounts:
      account_data = {
        'title': account.find('{http://www.w3.org/2005/Atom}title').text,
        'link': account.find('{http://www.w3.org/2005/Atom}link').text
      }
      for f in account.getiterator('{http://schemas.google.com/analytics/2009}property'):
        account_data[f.attrib['name']] = f.attrib['value']
      a = Account(
        connection=self,
        title=account_data['title'],
        link=account_data['link'],
        account_id=account_data['ga:accountId'],
        account_name=account_data['ga:accountName'],
        profile_id=account_data['ga:profileId'],
        web_property_id=account_data['ga:webPropertyId']
      )
    return render_to_response('TestData.html', {'random_value' : text} )


    def get_account(self, profile_id, validate=False):
        account = Account(connection=self, profile_id=profile_id)
        return account

    def parse_response(self, xml):
        from xml.etree import ElementTree
        tree = ElementTree.fromstring(xml)
        return tree

    def make_request(self, method, path, headers=None, data=''):
        if headers == None:
          headers = {
            'User-Agent': self.user_agent,
            'Authorization': 'GoogleLogin auth=%s' % self.auth_token 
          }
        else:
          headers = headers.copy()
         
        if DEBUG:
          print "** Headers: %s" % (headers,)
             
        if method == 'GET':
          path = '%s?%s' % (path, data)

        if DEBUG:
          print "** Method: %s" % (method,)
          print "** Path: %s" % (path,)
          print "** Data: %s" % (data,)
          print "** URL: %s" % (self.default_host+path)

        if method == 'POST':
          request = urllib2.Request(self.default_host + path, data, headers)
        elif method == 'GET':
          request = urllib2.Request(self.default_host + path, headers=headers)

        try:
          response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
          raise GoogleAnalyticsClientError(e)


                            
