def simple_coroutine(a):
    print('->start')
    b= yield a
    print('->received',a,b)
    c=yield a+b
    print('->received',a,b,c)

sr=simple_coroutine(5)

aa=next(sr)

print(aa)
bb=sr.send(6)
print(bb)
cc=sr.send(7)
print(cc)