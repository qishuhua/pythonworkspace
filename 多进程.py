#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import multiprocessing
import time
import os


def clock(interval):
    while True:
        print('the time is {}'.format(time.ctime()))
        time.sleep(interval)


def main1():
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()
    while True:
        print('sleep')
        time.sleep(3)


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        super(ClockProcess,self).__init__()
        self.interval = interval

    def run(self):
        while True:
            print('the time is {}'.format(time.ctime()))
            time.sleep(self.interval)
def main2():
    p=ClockProcess(3)
    p.start()

def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:',os.getppid())
    print('process id:',os.getpid())

def fun3(title):
    info(title)

def main3():
    info('main ')
    p=multiprocessing.Process(target=fun3,args=('child',))
    p.start()
    p.join()
if __name__ == '__main__':
    main3()
