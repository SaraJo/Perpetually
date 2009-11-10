from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
from models import top_url

def get_parse_list(request):
    page = urllib2.urlopen("http://www.quantcast.com/top-sites-1")
    soup = BeautifulSoup(page)
    rank = 1
    for link in soup.findAll(lambda tag: tag.name == 'a' and \
    tag.findParent('table', attrs={'class':'listing'})):
            if link.string is not None:
                u = top_url(url = link.string, rank = rank, date_added = datetime.datetime.now())
                u.save()
                rank = rank + 1
            
                              

