#!/usr/bin/python2.7
from bs4 import BeautifulSoup
import urllib2
import re
camvid = "http://www.camwhores.tv/search/sashapain/"
page = urllib2.urlopen(camvid)
soup = BeautifulSoup(page, 'lxml')
for elem in soup.find_all('a', href=re.compile('http://www\.camwhores\.tv/videos/')):
    print elem['href']
