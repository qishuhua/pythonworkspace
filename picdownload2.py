#!/usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import threading
import time
import sys
import os
import struct

FILE_PATH = 'd:\\datacenter\\campic\\'
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.bind(('218.95.37.66', 18884))  # 这里换上自己的ip和端口
        s.bind(('10.10.10.105', 18884))  # 这里换上自己的ip和端口
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print ("Waiting...")
    while 1:
        conn, addr = s.accept()
        conn.setblocking(1)
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    global FILE_PATH
    print ('Accept new connection from {0}'.format(addr))
    while 1:
        try:
            fileinfo_size = struct.calcsize('128sq')
            buf = conn.recv(136)
            if buf:
                filename, filesize = struct.unpack('128sq', buf)
                fn = filename.strip(str.encode('\00'))
                new_filename = os.path.join(str.encode(FILE_PATH), fn)
                print new_filename
                recvd_size = 0  # 定义已接收文件的大小
                alldata = 
                t = time.time()

                print ("start receiving...")
                while not recvd_size == filesize:
                    if time.time() - t > 5:
                        break
                    if filesize - recvd_size > 1024:
                        data = conn.recv(1024)
                        recvd_size += len(data)
                        alldata += data
                    else:
                        data = conn.recv(filesize - recvd_size)
                        recvd_size += len(data)
                        alldata += data
                if recvd_size == filesize:
                    fp = open(new_filename + '.jpg', 'wb')
                    fp.write(alldata)
                    fp.close()

        finally:
            print ("end receive...")
            conn.close()
        break


if __name__ == '__main__':
    socket_service()
