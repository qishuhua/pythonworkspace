import matplotlib.pyplot as plt 
import numpy as np 
import tensorflow as tf 
import pandas as pd

TRAIN_URL="http://download.tensorflow.org/data/iris_training.csv"
tarin_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)
COLUMN_NAMES=["SepalLength","SepalWidth","PatalLength",'PetalWidth','Speicies']
df_iris=pd.read_csv(tarin_path,header=0,names=COLUMN_NAMES)
iris=np.array(df_iris)
fig=plt.figure("Iris Data",figsize=(15,15))
fig.suptitle("Anderson's iris data set \n(bule->setosa|red->versicolor|Grern->virginica)",fontsize=20)
for i in range(4):
    for j in range(4):
        plt.subplot(4,4,4*i+(j+1))
        if(i==j):
            plt.text(0.3, 0.4, COLUMN_NAMES[i],fontsize=15)
        else:
            plt.scatter(iris[:,j], iris[:,i],c=iris[:,4],marker='.',cmap='brg')
        if i==0:
            plt.title(COLUMN_NAMES[j])
        if j==0:
            plt.ylabel(COLUMN_NAMES[i])
plt.show()
