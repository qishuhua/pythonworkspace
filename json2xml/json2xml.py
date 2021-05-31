#!/usr/bin/env python
# coding=utf-8
import json
import io
from xml.dom.minidom import Document
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

if len(sys.argv) != 3:
    exit('json path or xml path error')
try:

    jsonpath = sys.argv[1]
    xmlpath = sys.argv[2]
    src = open(jsonpath, 'r')
    obj = json.loads(src.read())
    if not obj.has_key('timestamp') or not obj.has_key('base_url') or not obj.has_key('audio_files'):
        exit('key not all exist')

    doc = Document()
    root = doc.createElement('MSG')
    doc.appendChild(root)

    META = doc.createElement('META')
    timestamp = doc.createElement('TIMESTAMP')
    timestamp.appendChild(doc.createTextNode(obj["timestamp"]))

    base_url = doc.createElement('BASEURL')
    base_url.appendChild(doc.createTextNode(obj["base_url"]))

    TYPE = doc.createElement('TYPE')
    TYPE.appendChild(doc.createTextNode('MTABLE'))

    META.appendChild(timestamp)
    META.appendChild(base_url)
    META.appendChild(TYPE)
    root.appendChild(META)

    if not isinstance(obj['audio_files'], list):
        exit('audio_files is not list')
    else:
        FQ = doc.createElement('FQ')
        for i in obj['audio_files']:
            Group = doc.createElement('GROUP')
            for j in i.keys():
                name = doc.createElement(j.upper())
                name.appendChild(doc.createTextNode(i[j]))
                Group.appendChild(name)
            FQ.appendChild(Group)
        root.appendChild(FQ)
    with open(xmlpath, 'w') as fp:
        doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
except Exception as e:
    exit(e)
