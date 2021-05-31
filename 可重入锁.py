#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'
import threading
import time



num=0
mutex=threading.Lock()
mutex=threading.RLock()#可重入锁
class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire(1):
            num+=1
            msg = self.name+'  set num to '+ str(num)
            print( msg)
            mutex.acquire()
            mutex.release()
            mutex.release()
def test1():
    for i in range(5):
        t=MyThread()
        t.start()

if __name__=="__main__":
    test1()