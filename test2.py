#!/usr/bin/env python
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import datetime
import time

filepath = 'd:\\datacenter\\hk197.jpg'
filename = "hk197"


def socket_client():
    global filename, filepath
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8000))
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while 1:
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', bytes(filename.encode('utf-8') + str(
                datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S.jpg").encode('utf-8'))),
                                os.stat(filepath).st_size)
            s.send(fhead)
            print ('client filepath: {0}'.format(filepath))
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(filepath))
                    break
                s.send(data)
        s.close()
        break


if __name__ == '__main__':
    t = 0
    while True:
        if time.time() - t > 5:
            t = time.time()
            socket_client()

