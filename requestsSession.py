#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: request.py
@time: 2018/10/13
"""
import requests
session=requests.session()
# 请求百度网页
response = session.get("https://www.baidu.com", data=None, timeout=10)
print(response.status_code)
print(response.headers)
print(response.text)

