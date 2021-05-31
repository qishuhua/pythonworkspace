#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import chardet
from urllib import request

url = 'https://www.163.com/'
if __name__ == '__main__':
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    print(html)
    html = html.decode(cs.get("encoding", 'utf-8'),'ignore')#ignore忽略非法字符
    print(html)
