from BeautifulSoup import BeautifulSoup
import urllib2
from models import top_url

def get_parse_list:
    page = urllib2.urlopen("http://www.quantcast.com/top-sites-1")
    soup = BeautifulSoup(page)
    table = soup.findAll('table', {"class" : "listing"})
    sites = BeautifulSoup(table)
    rank = 1
    for link in soup.findAll(lambda tag: tag.name == 'a' and \
    tag.findParent('table', attrs={'class':'listing'})):
            u = top_url(url= link.string, rank = rank, date_added = datetime.datetime.now())
            u.Save
            rank = rank + 1
            
                              

