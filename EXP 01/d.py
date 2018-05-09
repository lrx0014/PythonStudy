import math

a=int(input('input a:'))
b=int(input('input b:'))
c=int(input('input c:'))

s=(a+b+c)/2

A=s*(s-a)*(s-b)*(s-c)
if A<=0:
    print('this is not a triangle')
else :
    if a==b and b==c :
        print('this is a regular triangle and its area is '+str(math.sqrt(A)))
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        if a==b or a==c or b==c:
            print('this is an isoceles right triangle and its area is '+str(math.sqrt(A)))
        print('this is a right-angled triangle and its area is '+str(math.sqrt(A)))
    elif a==b or a==c or b==c:
        print('this is an isoceles triangle and its area is '+str(math.sqrt(A)))
    else:
        print('this is a triangle and its area is '+str(math.sqrt(A)))

        