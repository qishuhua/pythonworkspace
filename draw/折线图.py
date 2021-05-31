import matplotlib.pyplot as plt 
import numpy as np 
plt.rcParams['font.sans-serif']='SimHei'

n=24
y1=np.random.randint(27,37,n)
y2=np.random.randint(40,60,n)

plt.plot(y1,label='温度')
plt.plot(y2,label='湿度')
plt.xlim(0,23)
plt.ylim(20,70)
plt.xlabel('小时',fontsize=14)
plt.ylabel('测量量',fontsize=14)
plt.title('24小时温湿度统计',fontsize=16)
plt.show()