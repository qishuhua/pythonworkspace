# coding =utf-8
__author__='qishuhua'
import os
import threading
import time
from Queue import Queue
import subprocess


dict = {}

lock=threading.Lock()
onlinenum=0
def insert_ip_queue():
    IP_QUEUE = Queue()
    list = ['192.168.10.%d' % (x) for x in range(1, 225)]
    # list = ['172.16.3.%d' % (x) for x in range(1, 225)]
    for host in list:
        IP_QUEUE.put(host)
    return IP_QUEUE


def ping_host(IP_QUEUE):
    global onlinenum
    while not IP_QUEUE.empty():
        try:
            ip = IP_QUEUE.get_nowait().strip("\n")
            popen = subprocess.Popen('ping -n 1 -w 1 %s' % ip, stdout=subprocess.PIPE, shell=True)
            popen.wait()
            res = popen.stdout.read()
            if "TTL" in res:
                res = 1
                lock.acquire()
                onlinenum+=1
                lock.release()
            else:
                res = 0
            out, err = popen.communicate()
        except Exception as error:
            return


if __name__ == "__main__":
    while 1:
        IP_QUEUE = insert_ip_queue()
        t_thread = []
        for i in range(30):
            thread = threading.Thread(target=ping_host, args=(IP_QUEUE,))
            thread.start()
            t_thread.append(thread)
        for i in t_thread:
            i.join()
        lock.acquire()
        print time.ctime(),'online num:',onlinenum,'thread num:',threading.active_count()
        onlinenum=0
        lock.release()
        time.sleep(10)
