arr=[]
while True :
    a=int(input('input:'))
    if a==0:
        break
    else :
        arr.append(a)

s=0
for i in arr:
    if i%2==0:
        s+=i
        
print('SUM:  '+str(s))

