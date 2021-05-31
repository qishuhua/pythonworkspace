import matplotlib.pyplot as plt 
import numpy as np 
import tensorflow as tf 

plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False

boston_housing=tf.keras.datasets.boston_housing
(train_x,train_y),(_,_)=boston_housing.load_data(test_split=0)
titles=["CRIM",'ZN',"INDUS","CHAS","NOX","RM","AGE",'DIS','RAD',"TAX",'PTRATIO','B-1000','LSTAT','MEDV']
plt.figure(figsize=(12,12))

for i in range(12):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($100's)")
    plt.title(str(i+1)+'.'+titles[i]+' - price')
plt.tight_layout(rect=[0,0,1,0.96])
plt.suptitle("各属性与房价关系",x=0.5,y=1.0,fontsize=20)
plt.show()