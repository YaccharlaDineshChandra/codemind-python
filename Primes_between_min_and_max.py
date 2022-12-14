import math
def prime(x):
    if x==0 or x==1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True            
n=int(input())
l=list(map(int,input().split()))
a=l.index(min(l))
b=l.index(max(l))
count=0
if a<b:
    for i in range(a,b+1):
        if prime(l[i])==True:
            count=count+1
else:
    for i in range(b,a+1):
        if prime(l[i])==True:
            count=count+1
print(count)