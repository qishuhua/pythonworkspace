#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import xml.dom.minidom

domtree = xml.dom.minidom.parse(r'../logconfig.xml')
doc = domtree.documentElement
print(doc)
if doc.hasAttribute('ChkCfgMdfyPeriod'):
    print('ChkCfgMdfyPeriod:{}'.format(doc.getAttribute('ChkCfgMdfyPeriod')))
    print(len(doc.childNodes))
for ele in doc.childNodes:
    print(ele)
    if ele.nodeName == 'General':
        if ele.hasAttribute('CurrentLogLV'):
            print('CurrentLogLV:{}'.format(ele.getAttribute('CurrentLogLV')))
        if ele.hasAttribute('SaveDays'):
            print('SaveDays:{}'.format(ele.getAttribute('SaveDays')))
        if ele.hasAttribute('FileMaxKb'):
            print('FileMaxKb:{}'.format(ele.getAttribute('FileMaxKb')))
        if ele.hasAttribute('FileMaxNo'):
            print('FileMaxNo:{}'.format(ele.getAttribute('FileMaxNo')))
        if ele.hasAttribute('LogOnMonitor'):
            print('LogOnMonitor:{}'.format(ele.getAttribute('LogOnMonitor')))

import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse(r'../logconfig.xml')

nodes = tree.getiterator()
for node in nodes:
    print('----------------------------------')
    print('{0}---{1}'.format(node.tag, node.text))
    if node.tag == 'General':
        if "CurrentLogLV" in node.attrib.keys():
            print('CurrentLogLV:', node.attrib['CurrentLogLV'])
        if "SaveDays" in node.attrib.keys():
            print('SaveDays：', node.attrib['SaveDays'])
        if "FileMaxKb" in node.attrib.keys():
            print('FileMaxKb：', node.attrib['FileMaxKb'])
        if "FileMaxNo" in node.attrib.keys():
            print('FileMaxNo：', node.attrib['FileMaxNo'])
        if "LogOnMonitor" in node.attrib.keys():
            print('LogOnMonitor：', node.attrib['LogOnMonitor'])


