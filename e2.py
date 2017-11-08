#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

website = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'

req = requests.get(website)
html = req.content #getting the contents of the website
soup = BeautifulSoup(html,'html.parser') #turning it into a soup object so you can manipulate in python
tags = soup.find_all('tr','election_item')

ELECTION_ID=[]
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    i=[year, year_id]
    ELECTION_ID.append(i)

    #print(year, year_id)
year_1 = [item[0] for item in ELECTION_ID]
year_id = [item[1] for item in ELECTION_ID]
dictionary = dict(zip(year_id, year_1))
dictionary

for l in year_id:
    base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
    replace_url = base.format(l)
    response = requests.get(replace_url).text
    data_files = "president_general_"+ dictionary[l] +".csv"
    with open(data_files, 'w') as output:
        output.write(response)
