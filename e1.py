#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

website = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'

req = requests.get(website)
html = req.content #getting the contents of the website
soup = BeautifulSoup(html,'html.parser') #turning it into a soup object so you can manipulate in python

#find 'tr' tags with class 'election_item because these contain the ID'
tags = soup.find_all('tr','election_item')

ELECTION_ID=[]
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    i=[year, year_id]
    ELECTION_ID.append(i)
    print(year, year_id)

with open('ELECTION_ID','w') as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + ' ' + line[1])
        print(line[0],line[1])
