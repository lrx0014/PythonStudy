import datetime
import random

# ‘+’运算符
AList = []
begin = datetime.datetime.now()
for x in range(10000):
    AList += [x]
end = datetime.datetime.now()
print('+ 运算符: ', end-begin)

# append()
BList = []
begin = datetime.datetime.now()
for y in range(10000):
    BList.append(int(y))
end = datetime.datetime.now()
print('append(): ', end-begin)

# insert()
CList = []
begin = datetime.datetime.now()
for z in range(10000):
    CList.insert(0, int(z))
end = datetime.datetime.now()
print('insert(): ', end-begin)

DList = []
for i in range(10000):
    DList.append(i)
random.shuffle(DList)

_Sort = DList
begin = datetime.datetime.now()
_Sort.sort()
end = datetime.datetime.now()
print('  sort(): ', end-begin)

_Sort = DList
begin = datetime.datetime.now()
sorted(_Sort)
end = datetime.datetime.now()
print('sorted(): ', end-begin)
