def gen():
    for c in "ab":
        yield c
print(list(gen()))

def gen_new():
    yield from 'ab'
print(list(gen_new()))
#yeild from 每次从后面的元素中返回一个