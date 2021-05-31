#coding =utf-8
import time
import logging
import os
from logging import handlers
import sys


def _logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('format', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:
        filename = 'default.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s %(levelname)s [%(lineno)d] %(message)s'

    log = logging.getLogger(filename)
    format_str = logging.Formatter(format, datefmt)
    th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=3, encoding='utf-8')
    th.setFormatter(format_str)
    th.suffix = "%Y-%m-%d.log"
    ch=logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(format_str)
    log.addHandler(ch)
    log.addHandler(th)
    log.setLevel(level)
    return log





if __name__ == '__main__':
    os.makedirs("./logs", exist_ok=True)
    filename = os.path.basename((sys.argv[0])).split('.')[0] + '.txt'
    print(filename)

    logger = _logging(filename='./logs/' + filename,level = logging.DEBUG)
    logger.info('logger.info')
    logger.error(' logger.error')
    logger.debug(' logger.debug')
