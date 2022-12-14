import math
def prime(x):
    if x==0 or x==1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True            
            
m=int(input())
n=int(input())
count=0
for i in range(m,n+1):
    if prime(i)==True:
        count=count+1
print(count)