#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

from urllib import request,parse
import json


if __name__=='__main__':
    url='https://fanyi.baidu.com/sug'
    keword=input('请输入查询关键词：\n')
    data={
        'kw':keword
    }
    data=parse.urlencode(data).encode("utf-8")
    print(type(data))

    headers={
        'Content-Length':len(data)
    }
    rsp=request.urlopen(url,data=data)
    json_data=rsp.read().decode()
    json_data=json.loads(json_data)
    print(json_data)
    for item in json_data['data']:
        print(item['k'],'--',item['v'])