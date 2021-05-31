#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request,error
import json


if __name__=='__main__':
    url='https://www.baidu.com'
    try:
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }


        req=request.Request(url=url,headers=headers)

        # req.add_header("User-Agent",'-----')

        rsp=request.urlopen(req)
        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError', e.reason, '====', e)
    except error.URLError as e:
        print('URLError', e.reason, '====', e)
    except Exception as e:
        print(e)