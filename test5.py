num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'A': 10, 'b': 11,
       'B': 11, 'c': 12, 'C': 12, 'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}

value = '64646464ffffffffffff'

for i in range(12):
    a = num[value[8 + i]]
    name1 = 'loop%02d' % (5 + 4 * i)
    name2 = 'loop%02d' % (5 + 4 * i + 1)
    name3 = 'loop%02d' % (5 + 4 * i + 2)
    name4 = 'loop%02d' % (5 + 4 * i + 3)
    value1 = a >> 3 & 0x0001
    value2 = a >> 2 & 0x0001
    value3 = a >> 1 & 0x0001
    value4 = a & 0x0001
    print name1, value1, name2, value2, name3, value3, name4, value4
