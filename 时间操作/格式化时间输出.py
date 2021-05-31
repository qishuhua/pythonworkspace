import time
from datetime import datetime

time1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("strftime:", time1)
print(datetime.now().strftime("%Y%m%d%H%M%S"))

t = datetime.now()

print(t.year, t.month, t.day, t.hour, t.minute, t.second)

print('time.ctime():', time.ctime())
