#!/usr/bin/env python
# -*- coding=utf-8 -*-

import socket
import os
import sys
import struct
import datetime
import time


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6000))
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    while 1:
        recv = s.recv(2048)
        recv = recv.decode('gbk')
        print repr(recv)
        print type(recv)
        print len(recv)
        break


if __name__ == '__main__':
    t = '111'
    print len(t.split('|'))
    t = 0
    while 1:
        socket_client()
