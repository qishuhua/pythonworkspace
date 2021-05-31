#! /usr/bin/python
# coding=utf-8
from ftplib import FTP
import time,tarfile,os
import cv2
import time
import datetime
import os

Picturename=""
picturePath=""

#截图
def  getpictue( ):
    global picturePath
    cap=cv2.VideoCapture("rtsp://admin:1qaz2wsx@192.168.10.198:554/h264/ch1/sub/av_stream")
    while True:
        ret, frame=cap.read()		
        if cv2.imwrite(picturePath, frame):# 存储为图像
            break
    cap.release()
    cv2.destroyAllWindows()
#连接ftp
def ftpconnect(host,port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置的缓冲区大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)# 参数为0，关闭调试模式
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":

    shottime=0
    uploadtime=0
    while True:
        if time.time()-shottime>10:
            shottime=time.time()
            if (os.path.exists(picturePath)):
                os.remove(picturePath)
            Picturename="hk198-"+str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))
            picturePath='E://datacenter//campic//'+Picturename+'.jpg'
            getpictue()
        if time.time()-uploadtime>120:
            uploadtime=time.time()
            ftp = ftpconnect("218.95.37.66", 18883,"admin", "admin")
            uploadfile(ftp, Picturename,picturePath)
            ftp.close() #关闭ftp
