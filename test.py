import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

def Calc(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)
    return
S = Calc(1,2,3,4,5,6)
print(S)
