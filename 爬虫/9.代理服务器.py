#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request,error
if __name__=='__main__':
    url='https://www.goubanjia.com'
    proxy={
        'http':'60.184.110.80:3000'
    }
    proxy_hander=request.ProxyHandler(proxy)
    opener=request.build_opener(proxy_hander)
    request.install_opener(opener)
    try:
        rsp=request.urlopen('https://www.baidu.com')
        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print('HTTPError', e.reason, '====', e)
    except error.URLError as e:
        print('URLError', e.reason, '====', e)
    except Exception as e:
        print(e)