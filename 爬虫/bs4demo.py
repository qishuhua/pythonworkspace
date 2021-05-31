
__author__ = 'qishuhua'
import requests
from  bs4 import BeautifulSoup
url='https://www.baidu.com'
rsp=requests.get(url)
context=rsp.text
soup=BeautifulSoup(context,'lxml')
import re

tags=soup.find_all(re.compile('^me'),content='always')
for i in tags:
    print(i)

titles=soup.select('title')
print(titles[0])

metas=soup.select("meta[content='always']")
print(metas[0])