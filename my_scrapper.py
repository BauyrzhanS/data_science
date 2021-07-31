import pip
pip.main(['install', 'requests'])
pip.main(['install', 'bs4'])
pip.main(['install', 'lxml'])

import requests as req
from bs4 import BeautifulSoup as bs

def my_req_get(path):
    return req.get(path)

def my_scraper(path):    
    soup = bs(my_req_get(path).text, 'lxml')
    print(soup.prettify())

    
path = "https://github.com/trending"
my_scraper(path)
