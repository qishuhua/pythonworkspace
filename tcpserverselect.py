# !/usr/bin/env python3
# coding =utf-8
import socket
import queue
import select
import os
import struct
import threading

HOST = '10.10.10.105'
PORT = 18884
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.10.10.105', 18884))
s.listen(40)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(0)

inputs = []
outputs = []

msg_dic = {}
inputs.append(s)
FILE_PATH = 'd:\\datacenter\\campic\\'
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)


def recv_data(conn, addr):
    global FILE_PATH, inputs
    fileinfo_size = struct.calcsize('128sq')
    print "fileinfo_size", fileinfo_size
    buf = conn.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('128sq', buf)
        fn = filename.strip(str.encode('\00'))
        new_filename = os.path.join(str.encode(FILE_PATH), fn)
        print ('file new name is {0}, filesize is {1}'.format(new_filename, filesize))
        print ("start receiving...")
        fp = open(new_filename + '.jpg', 'wb')
        recvd_size = 0
        print ("start receiving...")
        while not recvd_size == filesize:
            if filesize - recvd_size > 1024:
                data = conn.recv(1024)
                recvd_size += len(data)
            else:
                data = conn.recv(filesize - recvd_size)
                recvd_size = filesize
            fp.write(data)
        fp.close()
        print ("end receive...")
        return
    else:
        print("client disconnect")
        inputs.remove(r)
        r.close()
        return


while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is s:
            conn, addr = s.accept()
            print("new connect:", addr)
            conn.setblocking(0)
            inputs.append(conn)
        else:
            try:
                t = threading.Thread(target=recv_data, args=(conn, conn.getpeername()))
                t.start()
                continue
                print len(inputs), conn.getpeername()
                fileinfo_size = struct.calcsize('128sq')
                buf = conn.recv(fileinfo_size)
                if buf:
                    filename, filesize = struct.unpack('128sq', buf)
                    fn = filename.strip(str.encode('\00'))
                    new_filename = os.path.join(str.encode(FILE_PATH), fn)
                    print ('file new name is {0}, filesize is {1}'.format(new_filename, filesize))
                    print ("start receiving...")
                    fp = open(new_filename + '.jpg', 'wb')
                    recvd_size = 0
                    print ("start receiving...")
                    while not recvd_size == filesize:
                        if filesize - recvd_size > 1024:
                            data = conn.recv(1024)
                            recvd_size += len(data)
                        else:
                            data = conn.recv(filesize - recvd_size)
                            recvd_size = filesize
                        fp.write(data)
                    fp.close()
                    print ("end receive...")
                else:
                    print("client disconnect")
                    if r in outputs:
                        outputs.remove(r)
                    inputs.remove(r)
                    r.close()
            except socket.error:
                pass
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        e.close()

s.close()
