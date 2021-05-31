#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import re

'''
.(点)表示任意字符
[]:匹配中括号中列举的任意字符
\d:任意数字
\D:非数字
\s:空格，tab
\S:非空白符
\w:单词字符： a-z,A-Z,0-9,_
\W:非单词字符
*:表示前面字符出现0次或者多次    \w*:多个单词字符
+：至少一次
?:0次或者1次
{m,n}:前面内容最少出现m次，最多出现n次
^:匹配字符串开始
$:匹配字符串结束
\b：匹配单词的边界
()：对正则表达式内容进行分组

                    一个数字：^\d$
                    至少一个数字：^\d+$
                    只能出现数字，且位数在5-10位：^\d{5,10}$
                    年龄16以上，9以下 ^[16-99]$
                    只能输入英文字符和数字：^[a-zA-Z0-9]$
                    验证QQ号：[0-9]{5,12}
    
    
\A：只能匹配字符串开头 \Aabcd 则abcd
\Z: 只能匹配字符串末尾 \Dabcd,abcd
|:左右任意一个

[u4e00-u9fa5] 大部分中文

'''

p = re.compile(r'\d+')
m=p.search('i fdsaf ifd')#只查找一个
print(m)

p2 = re.compile(r'([a-z]+) ([a-z]+)',re.I)
m=p2.match('i fdsaf ifd')
print(m.groups())
print(m.group())
print(m.group(0))
print(m.group(1))
'''
search(str,[pos[,endpos]])
'''
res=p.findall('0dfa321nnasdf')
print(type(res))
print(res)

p3=re.compile(r'([a-zA-Z]+) ([a-zA-Z]+)')
s = 'jok fjoij ii ff fdsf fff '
res=p3.sub(r'111',s)
print(res)

title=u'你还 实际，hello'
p=re.compile(r'[\u4e00-\u9fa5]+')
res=p.findall(title)
print(res)

p=re.compile(r'h(.*?)')
res=p.findall(title)
print(res)