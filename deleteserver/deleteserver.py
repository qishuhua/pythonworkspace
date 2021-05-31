import os
import sys
import socket
import datetime
import time
import cx_Oracle
import configparser

gConf=None

def readConf():
    global gConf
    conf= configparser.ConfigParser()
    conf_path=os.path.join("/home/user/warningfile",'deleteserver.ini')
    if not os.path.isfile(conf_path):
        print(conf_path,"文件不存在")
        return None
    conf.read(conf_path) # 文件路径
    try:
        DB_user = conf.get("DB", "user") 
        DB_pwd = conf.get("DB", "pwd") 
        DB_param = conf.get("DB", "param")
        videopath=conf.get("DB", "videopath")
        imagepath=conf.get("DB", "imagepath")
        gConf=(DB_user,DB_pwd,DB_param,videopath,imagepath)
        return gConf
    except Exception as e:
       return None

def DeleteHis(ip,date):
    if gConf is None:
        return
    conn=cx_Oracle.connect(gConf[0],gConf[1],gConf[2])
    cursor = conn.cursor()
    #1根据ip找出电脑设备ID
    sql="select ID from T_BASE_SERVER where IP='{}'".format(ip)  
    cursor.execute(sql)
    list_server_id=cursor.fetchall()
    if len(list_server_id) !=1:
        return
    #根据电脑iD找出所有摄像头设备iD
    sql="select ID from T_BASE_VIDEO_CHANNEL where SERVER_ID={}".format(list_server_id[0][0])
    cursor.execute(sql)
    list_Device_ID=cursor.fetchall()
    if len(list_Device_ID) is None:
        return
    #根据摄像头设备id和时间找出记录
    for i in range(len(list_Device_ID)):
        sql="delete  from T_BASE_EVENT where CAM_ID={0} and BJSJ  LIKE '{1}%'".format(list_Device_ID[i][0],date)    
        cursor.execute(sql)
        print("删除第{}条记录".format(i))
    conn.commit()
    cursor.close()
    conn.close()

def GetIP():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    except:
        ip=''
    finally:
        s.close()
    return ip

def GetHomeDiskUse():
    statvfs = os.statvfs('/home')
    total_disk_space = statvfs.f_frsize * statvfs.f_blocks
    free_disk_space = statvfs.f_frsize * statvfs.f_bfree
    disk_usage = (total_disk_space - free_disk_space) * 100.0 / total_disk_space
    return  disk_usage

def DateCompare(date1, date2, fmt='%Y%m%d') -> bool:
    zero = datetime.datetime.fromtimestamp(0)
    try:
        d1 = datetime.datetime.strptime(str(date1), fmt)
    except:
        d1 = zero
    try:
        d2 = datetime.datetime.strptime(str(date2), fmt)
    except:
        d2 = zero
    return d1 < d2

def GetMinFolerName(path):
    print("开启获取{}路径下最小文件夹".format(path))
    lists=os.listdir(path)
    lists.sort()
    if len(lists)<=0:
        print("{}路径下没有任何文件夹存在".format(path))
        return None
    for stri in lists:
        if len(stri)!=8:
            RemovePath(stri)
            lists.remove(stri)
    lists=os.listdir(path)
    for i  in range(len(lists)):
        if  DateCompare(lists[i],ret):
            ret=lists[i]
    return  ret

def Task(ListPath): 
    print(ListPath)  
    if not os.path.isdir(ListPath):
        print(ListPath,"路径不存在")
        return 
    folername=GetMinFolerName(ListPath)
    if folername is None:
        print("未找到最小文件夹")
        return
    #递归删除video文件
    videopath=os.path.join(ListPath,folername)
    RemovePath(videopath)
    print("delete size min dirname is:"+videopath)       
    #删除数据库记录
    ip=GetIP()
    date=folername[0:4]+'-'+folername[4:6]+'-'+folername[6:]
    print("开始删除数据库记录中ip含有{},date含有{}的数据".format(ip,date))
    DeleteHis(ip,date)

def RemovePath(dirpath):
    if os.path.exists(dirpath):
        files = os.listdir(dirpath)
        for file in files:
            filepath = os.path.join(dirpath, file).replace("\\",'/')
            if os.path.isdir(filepath):
                RemovePath(filepath)
            else:
                os.remove(filepath)
        os.rmdir(dirpath)

if __name__=='__main__':
    while True:
        gConf=readConf()
        while True:
            diskinfo=GetHomeDiskUse()
            if diskinfo>80:
                print("home盘使用率 {} > 80% ,将删除最旧目录".format(diskinfo))
                Task(gConf[3])
                Task(gConf[4])
            time.sleep(1000)
