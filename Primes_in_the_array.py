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
count=0
for i in l:
    if prime(i):
        count+=1
print(count)