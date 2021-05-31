#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import threading
import time

# 互斥锁和信号量示例
lock1=threading.Lock()
lock2=threading.Lock()





def func():
    print 'start func'
    time.sleep(4)
    print 'end func'
def main1():
    t = threading.Timer(6, func)#6秒后调用一次而已
    t.start()

    i = 0
    while True:
        print '{}____________________'.format(i)
        time.sleep(3)
        i += 1




def func1():
    print  'func1.start'
    ret=lock1.acquire(timeout=3)
    if ret:
        print 'get lock1'
        lock1.release()
    else:
        print 'not get lock1'






semphore=threading.Semaphore(3)
def func2():
    if semphore.acquire():
        print threading.current_thread().getName()+'get semaphore'
        time.sleep(5)
        semphore.release()
        print threading.current_thread().getName()+'release semaphore'

def main2():
    for i in range(8):
        t=threading.Thread(target=func2)
        t.start()
        time.sleep(1)










if __name__ == '__main__':
    main2()
