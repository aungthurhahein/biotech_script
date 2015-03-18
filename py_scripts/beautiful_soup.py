__author__ = 'Aung'

import sys
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
r = http.request('GET','http://aungthurhahein.github.com/typoem/index.html')
soup = BeautifulSoup(open(r.data))
print soup.div.p.a
# print(soup.find_all('p'))
