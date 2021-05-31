#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'
import ssl
from urllib import request

ssl.create_default_https_context=ssl._create_unverified_context
url='https://www.12306.cn/index/'
rsp=request.urlopen(url)
html=rsp.read().decode()
print(html)