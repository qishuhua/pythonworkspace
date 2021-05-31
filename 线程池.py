import concurrent.futures
import time
def return_future(msg):
    time.sleep(3)
    return msg
pool=concurrent.futures.ThreadPoolExecutor(max_workers=4)

f1=pool.submit(return_future,'hello')
f2=pool.submit(return_future,'world')
print(f1.done())
time.sleep(3)
print(f2.done())
print(f1.result())
print(f2.result())

#map案例
import re,os,datetime

data=['1','2','3','4','5']
def wait_on(argument):
    print(argument)
    time.sleep(2)
    return 'OK'

ex=concurrent.futures.ThreadPoolExecutor(max_workers=4)
for i in ex.map(wait_on,data):
    print(i)