#!/usr/bin/env python
from flask import Flask, request, Response
import pymysql
import hashlib
import base64

app = Flask(__name__)

SALT="1qaz2wsx"

def SQLquery(username):
    password=""
    ret=0
    db = pymysql.connect(host="localhost",port=3306,user="root",password="admin",database="peak" ,charset='utf8')
    cursor=db.cursor()
    sql="select password from t_video_user where username= '%s'"%(username)
    print(sql)
    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        password=results[0][0].replace('\r','').replace('\n','').replace(' ','')    
    except:
        print("error:unable to fetch data" )
        ret=-1
        password=""
    finally:
        db.close()
        return(ret,password)

def MD5andbase64encode(strText):
    global SALT
    strText=strText+SALT
    print("加密前数据:",strText)
    md=hashlib.md5()
    md.update(strText.encode("utf-8"))
    strmd5=md.hexdigest()
    print("md5加密后:",strmd5)
    strBase64=str(base64.urlsafe_b64encode(strmd5.encode("utf-8")),"utf8")
    print("base64加密后:",strBase64)
    return strBase64

#传入url格式为: xx.xx.xx.xx:10078/user/publish?username=xxx&password=xxx
@app.route('/publish',methods=['POST','GET'])
def publish():
    user = request.form['username']
    password = request.form['password']
    print("推流用户名:",user,"\r\n密码:",password)
    ret=SQLquery(user)
    if ret[0] != 0:
        return Response(response='username error',status=400)
    strEncode=MD5andbase64encode(ret[1])
    if strEncode ==password:
        return Response(response='success',status=200)
    else:
        return Response(response='password error',status=500)
        #Flask.abort(404)

@app.route('/play',methods=['POST','GET'])
def play():
    user = request.form['username']
    password = request.form['password']
    print("拉流用户名:",user,"\r\n密码:",password)
    ret=SQLquery(user)
    if ret[0] != 0:
        return Response(response='username error',status=400)
    strEncode=MD5andbase64encode(ret[1])

    if strEncode ==password:
        return Response(response='success',status=200)
    else:
        return Response(response='password error',status=500)
        #Flask.abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=10078,debug=False)