#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request, error, parse
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = 'http://kms.peakinfo.cn:280/dologin.action'
    data = {
        'os_username': 'qishuhua',
        'os_password': 'qishuhua'
    }
    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())
    rsp = opener.open(req)


def gethomepage():
    url = 'http://kms.peakinfo.cn:280/#all-updates'
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html', 'w') as a:
        a.write(html)


if __name__ == '__main__':
    login()
    print(cookie)
    gethomepage()
