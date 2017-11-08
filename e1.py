#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

ELECTION_ID = [] #creating a list for
webpage = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
req = requests.get(webpage)
scrape = req.content #scraping the data from the website
soup = bs(scrape,'html.parser') #making a soup object to work with python
tags = soup.find_all("tr","election_item")

for t in tags:
    year = t.td.text
    year_id = t["id"][-5:]
    i = [year, year_id]
    ELECTION_ID.append(i)

with open("ELECTION_ID","w") as ELECTION_ID_file:
    for line in ELECTION_ID:
        ELECTION_ID_file.write(line[0] + " " + line[1] + "\n")
        print(line[0],line[1])
