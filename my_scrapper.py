import pip
pip.main(['install', 'requests'])
pip.main(['install', 'bs4'])
pip.main(['install', 'lxml'])

import requests as req
from bs4 import BeautifulSoup as bs

def request_github_trending(url):
    return req.get(url)

def find_all(soup, d):    
    return soup.find_all(d)

def find_one(find_data, f_tag, f_attr="", f_attr_text=""):
    return find_data.find(f_tag, attrs={f_attr:f_attr_text})

def mydef(tag):
    if (tag.name == "article" and "Box-row" in tag.attrs["class"]):           
        return tag

def transform(data):
    ret_data=[]
    for item in data:
        dict = {}        
        item_data = []
        
        ret_item = find_one(item, "div", "class", "f6 color-text-secondary mt-2")
        ret_item = find_one(ret_item, "span", "class", "d-inline-block mr-3")
        ret_item = find_all(ret_item, "a")
        for item2 in ret_item:
            item_data.append(str(item2["href"]).replace("/", ""))
        dict["developer"] = item_data
        
        ret_item = find_one(item, "h1", "class", "h3 lh-condensed")
        ret_item = find_one(ret_item, "a")
        item_data = ret_item["href"]
        dict["repository_name"] = item_data
    
        ret_item = find_one(item, "div", "class", "f6 color-text-secondary mt-2")
        ret_item = find_one(item, "a", "class", "Link--muted d-inline-block mr-3")
        item_data = str(ret_item.text).replace(" ", "").replace("\n", "").replace(",", "")
        dict["nbr_stars"] = item_data
        
        ret_data.append(dict)
    
    return ret_data
    
def ret_lang(soup):    
    lang = soup.body        
    lang = find_one(lang, "div", "class", "application-main")
    lang = find_one(lang, "main", "id", "js-pjax-container")
    lang = find_one(lang, "div", "class", "position-relative container-lg p-responsive pt-6")
    lang = find_one(lang, "div", "class", "Box")
    lang = find_one(lang, "div", "class", "Box-header d-md-flex flex-items-center flex-justify-between")
    lang = find_one(lang, "div", "class", "d-sm-flex flex-items-center flex-md-justify-end mt-3 mt-md-0 table-list-header-toggle ml-n2 ml-md-0")
    lang = find_one(lang, "div", "class", "position-relative mb-3 mb-sm-0")
    lang = find_one(lang, "details", "class", "details-reset details-overlay select-menu select-menu-modal-right hx_rsm")
    lang = find_one(lang, "summary", "class", "btn-link select-menu-button")
    lang = find_one(lang, "span")
    lang = str(lang.text).replace(" ", "").replace("\n", "")
    #print(f"Язык: {lang}")

def format(data):
    ret_str = ",".join(data[1]) + "\n"
    for i in data:
        for j in i:            
            if (isinstance(i[j], list)):
                ret_str += "'" + ",".join(i[j]) + "'"
            else:
                ret_str += "," + i[j]
        ret_str += "\n"
    return ret_str 
    
def my_scraper(url):    
    soup = bs(request_github_trending(url).text, 'lxml')
    ret_lang(soup)
    
    data = find_all(soup, mydef)
    data = transform(data)
    print(format(data))
    #print(soup.prettify()) вывести весь html код

url = "https://github.com/trending"
my_scraper(url)
