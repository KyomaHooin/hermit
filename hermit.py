#!/usr/bin/python3
#
# HRK 
#

import requests,lxml.html,time,sys
from urllib.parse import quote
from io import StringIO

ITEM='https://roztoky-kontaktni-cocky.heureka.cz/ursapharm-hylo-fresh-10-ml/'
SUFFIX="#prehled/?sort-filter=lowest_price"

session = requests.Session()

req = session.get(ITEM + SUFFIX)
p = lxml.html.HTMLParser()
t = lxml.html.parse(StringIO(req.text), p)
print(req.status_code)
if req.status_code == 200:
    data = t.xpath('//a[@class="c-offer__price-box"]')
    print(data)

