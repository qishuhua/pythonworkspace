#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'
from urllib import request
import chardet
if __name__=='__main__':
    url='https://www.zhaopin.com/shanghai/'
    rsp=request.urlopen(url)
    html=rsp.read()
    html=html.decode()
    print(html)