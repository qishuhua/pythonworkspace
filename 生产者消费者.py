#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'

import time
import multiprocessing


def consumer(input_q):
    print("info consumer", time.ctime())
    while True:
        item = input_q.get()
        print('pull', item, 'out of queue')
        input_q.task_done()
    print('out of consumer', time.ctime())#########################q.join()收到4个task-done信号后，主进程启动，立刻结束


def producer(sequence, ouput_q):
    print("info producer", time.ctime())
    for item in sequence:
        ouput_q.put(item)
        print('Put', item, 'into_q')
    print('out of producer', time.ctime())


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    proc = multiprocessing.Process(target=consumer, args=(q,))
    proc.daemon = True
    proc.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.join()
