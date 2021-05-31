#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'
from urllib import request,parse
if __name__=='__main__':
    url='https://www.baidu.com/s?'
    wd=input('input your keyword:\n')
    qs={
        'wd':wd
    }
    qs=parse.urlencode(qs)


    fullurl=url+qs
    print(fullurl)
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp.getcode())
    html=rsp.read()
    html=html.decode()
    print(html)