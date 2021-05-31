#!/usr/bin/python
# coding=utf-8
__author__ = 'qishuhua'
import pkloger
import sys
import os
import time
import logging


logger = pkloger._logging(filename='./logs/logdemo',level = logging.INFO)


def fun1():
    logger.info('fun1')
def fun2():
    logger.error('fun2')

def fun3():
    logger.debug('fun3')
if __name__ == '__main__':
    while True:
        fun1()
        fun2()
        fun3()
        time.sleep(1)