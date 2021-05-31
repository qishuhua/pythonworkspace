#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'


import time
import multiprocessing


def consumer(input_q):
    print("info consumer", time.ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of queue')
    print('out of consumer', time.ctime())#########################q.join()收到4个task-done信号后，主进程启动，立刻结束


def producer(sequence, ouput_q):
    print("info producer", time.ctime())
    for item in sequence:
        ouput_q.put(item)
        print('Put', item, 'into_q')
    print('out of producer', time.ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    proc = multiprocessing.Process(target=consumer, args=(q,))
    proc.start()

    proc2 = multiprocessing.Process(target=consumer, args=(q,))
    proc2.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
#多少个子进程，放多少个None
    q.put(None)
    q.put(None)
    proc.join()
    proc2.join()
