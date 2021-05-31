#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request,error
import json


if __name__=='__main__':
    url='https://yz.chsi.com.cn/ifff'
    try:
        req=request.Request(url)
        rsp=request.urlopen(req)
        html =rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError',e.reason,'====',e)
    except error.URLError as e:
        print('URLError',e.reason,'====',e)
    except Exception as e:
        print(e)