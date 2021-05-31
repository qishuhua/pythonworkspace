from collections import namedtuple

ResClass=namedtuple('res','count average')
def average():
    total=0.0
    count=0
    average=None
    while True:
        term=yield 
        if term is None:
            break
        total+=term
        count+=1
        average=total/count
    return ResClass(count,average)
def grouper(storages,key):
    while True:
        storages[key]=yield from average()
def client():
    process_data={
        'boys_2':[321,3,3,3,3,3,3,3,],
        'boys_1':[1,2,3,4,5,67,]
    }      
    storages={}
    for k,v in process_data.items():
        coroutine=grouper(storages,k)
        next(coroutine)
        for dt in v:
            coroutine.send(dt)
        coroutine.send(None)
    print(storages)

client()
