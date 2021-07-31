import requests as req
from bs4 import BeautifulSoup as bs

path = "https://github.com/trending"
my_scraper(path)


def my_req_get(path):
    return req.get(path)

def my_scraper(path):    
    soup = bs(my_req_get(path).text, 'lxml')
    print(soup.prettify())

    
