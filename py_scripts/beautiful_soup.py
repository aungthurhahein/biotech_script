# __author__ = 'Aung'

from bs4 import BeautifulSoup
import urllib3
import calendar
import datetime

now = datetime.datetime.now()
yyyy = str(now.year)
mmmm = str(now.month).zfill(2)
dddd = int(now.day)
folder= yyyy[2]+yyyy[3]+mmmm
# monthdays = calendar.monthrange(now.year, now.month)[1] #for the whole month

for x in range(1,dddd):
    dd = str(x).zfill(2)
    http = urllib3.PoolManager()
    r = http.request('GET','http://miniature-calendar.com/{0}/'.format(folder+dd))
    soup = BeautifulSoup(open(r.data))
    print(soup.prettify())
    # links = soup.find('post-body').find_all('img', src=True)
    # for link in links:
    #     link = link["src"].split("src=")[-1]
        # print link