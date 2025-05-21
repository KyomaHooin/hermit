#!/usr/bin/python3
#
# HRK 
#

import requests,sqlite3,lxml.html,time,sys
from urllib.parse import quote
from io import StringIO

FIREFOX='/home/*/.mozilla/firefox/z4fni3pa.default/cookies.sqlite'
ITEM='https://roztoky-kontaktni-cocky.heureka.cz/ursapharm-hylo-fresh-10-ml/'

SUFFIX="#prehled/?sort-filter=lowest_price"

headers={
'Host': 'roztoky-kontaktni-cocky.heureka.cz',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
'Accept-Language': 'cs,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'DNT': '1',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Priority': 'u=0, i',
'TE': 'trailers'
}

COOKIES={}

conn = sqlite3.connect(FIREFOX)
cur = conn.cursor()
cur.execute("SELECT name,value FROM moz_cookies WHERE host = '.heureka.cz'")
rows = cur.fetchall()
for name,value in rows: COOKIES[name] = value

print('[*] COOKIE: Ok')

session = requests.Session()

req = session.get(ITEM + SUFFIX, cookies=COOKIES, headers=headers)

print(req.status_code)

#if req.status_code == 200:
#    p = lxml.html.HTMLParser()
#    t = lxml.html.parse(StringIO(req.text), p)
#print(req.status_code)
#if req.status_code == 200:
#    data = t.xpath('//a[@class="c-offer__price-box"]')
#    print(data)

