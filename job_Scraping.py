import requests
import urllib.request
from bs4 import BeautifulSoup
import re
# url of job post from jobsarkari.com
url_text = 'https://www.jobsarkari.com/recruitment/jpsc-assistant-director-sr-scientific-officer-s/'
input_data = str(url_text)

page = urllib.request.urlopen(input_data)
soup = BeautifulSoup(page, 'html.parser')

[x.extract() for x in soup.findAll('script')]

# get desired data 
for a in soup.find_all('div', attrs={'id':'page'}):
	c = str(a)
	b= "table table-sm table-bordered w-100 border".join(c.split("table table-sm table-bordered w-100 border")[:-1])
	print(b)	
