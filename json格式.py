#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import json

student = {
    'name': 'qishuhua',
    'age': 1,
    'status': True
}
print(type(student))
stu_json = json.dumps(student)
print(type(stu_json))
print('json class{}'.format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)
print(type(stu_dict['status']))
with open(r'../t.json', 'w') as f:
    json.dump(stu_dict, f)
with open(r'../t.json', 'r') as f:
    d = json.load(f)
print(d)
