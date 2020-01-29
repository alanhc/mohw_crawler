import requests
import time
import urllib3
from bs4 import BeautifulSoup
import re
class Data_article:
    def __init__(self, head, article):
        self.head = head
        self.article = article

def crawler_page():
    urllib3.disable_warnings()
    r = requests.get('https://www.mohw.gov.tw/lp-4636-1.html',timeout=30,verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    links=[]
    for element in soup.findAll("a", title=re.compile('中央流行疫情指揮中心公布*')):
        link= element.get('href')
        links.append(link)
    #print(links)
    article = []
    for url in links:
        print('get',url)
        r = requests.get(url,timeout=30,verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        article.append(soup)
        time.sleep(2)
    
    data=[]
    for i in range(len(article)):
        header = article[i].section.find(class_="cp").h1.text
        ret=""
        ret = article[i].article.text
        ret = "".join(ret.split())
        #print(ret)
        data.append(Data_article(header,ret))
    return data
