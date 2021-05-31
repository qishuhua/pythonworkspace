from os.path import split,join,isdir,exists
from os import remove,listdir
from matplotlib import pyplot as plt 
from xml.dom.minidom import parse
from tkinter import Tk,filedialog,Button,LEFT,CENTER,messagebox


def draw(Folderpath,Sumdict,xmlnum,picnum):
    titlestr=Folderpath+"\n图片数:{} xml文件数量:{} 该目录下标图进度:{}".format(picnum,xmlnum,str(round(xmlnum*100/picnum))+"%")
    plt.rcParams['toolbar'] = 'None'
    figure = plt.figure('标注工作量统计图')
    plt.rcParams['font.sans-serif']='KaiTi'
    x=[]
    y=[]
    count=0
    for k,v in Sumdict.items():
        count=count+v
        x.append(k)
        y.append(v)
    x.append("count")
    y.append(count)
    p1 = plt.bar(x, height=y, width=0.1, tick_label=x)
    for a, b in zip(x, y):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.title(titlestr,fontsize=10)  
    plt.xlabel('标注类型')
    plt.ylabel('标注框数量')
    plt.show()

def GetFolerpath():
    Folderpath=filedialog.askdirectory()
    if Folderpath == '':
        return None
    filesPath=join(Folderpath,"Annotations")
    if not isdir(filesPath):
        messagebox.showwarning("获取目录失败",filesPath+"\n该路径不存在")
        return None
    return Folderpath

def calculation(filepath,Sumdict):
    try:
        domTree=parse(filepath)
        rootNode=domTree.documentElement
        objects=rootNode.getElementsByTagName("object")
        for obj in objects:
            name=obj.getElementsByTagName("name")[0].childNodes[0].data
            if name not in Sumdict:
                Sumdict[name]=0
            Sumdict[name]=Sumdict[name]+1
    except Exception as e:
        return

def log_calculation(filepath):
    domTree=parse(filepath)
    rootNode=domTree.documentElement
    objects=rootNode.getElementsByTagName("object")
    m_dict={}
    for obj in objects:
        name=obj.getElementsByTagName("name")[0].childNodes[0].data
        if name not in m_dict:
            m_dict[name]=0
        m_dict[name]=m_dict[name]+1
    filename=(split(filepath))[1]  
    with open("log.log","a+") as f:
        strone='['+filename+'] '
        for k,v in m_dict.items():
            strone=strone+"["+str(k)+":"+str(v)+"] "
        f.write("{}\n".format(strone))
    
def PraseXMLS():
    Folderpath=GetFolerpath()
    if Folderpath is None:
        return
    filesPath=join(Folderpath,"Annotations")
    picpath=join(Folderpath,"JPEGImages")
    fileslist=listdir(filesPath)
    piclist=listdir(picpath)
    xmlnum=len(fileslist)
    picnum=len(piclist)
    Sumdict={}
    for filename in fileslist:
        filepath=join(filesPath,filename)
        calculation(filepath,Sumdict)
    draw(Folderpath,Sumdict,xmlnum,picnum)

if __name__=="__main__":
    win =Tk()
    win.title("标注工作量")
    win.minsize(width = 300, height =100)
    win.resizable(0,0)
    btn=Button(win,text="请选择文件夹", command=PraseXMLS)
    btn.pack(padx=50,pady=50)
    win.mainloop()