import matplotlib.pyplot as plt 
import numpy as np 
plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False

n=24
y1=[32,25,16,30,24,45,40,33,28,17,24,20]
y2=[-23,-35,-26,-35,-45,-43,-35,-32,-23,-17,-22,-28]

plt.bar(range(len(y1)),y1,width=0.8,facecolor='g',edgecolor='w',label='统计量1')
# plt.bar(range(len(y2)),y2,width=0.8,facecolor='r',edgecolor='w',label='统计量2')

plt.title('柱状图',fontsize=20)
plt.show()