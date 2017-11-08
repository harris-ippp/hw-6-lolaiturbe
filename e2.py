#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

webpage = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
for line in open("ELECTION_ID", "r"):
    array = line.split(" ")
    year = array[0]
    election_id = array[1]
    file_name = year + ".csv"
    url = webpage.format(election_id)

    with open(file_name, "w") as output:
        output.write(requests.get(url).text)
