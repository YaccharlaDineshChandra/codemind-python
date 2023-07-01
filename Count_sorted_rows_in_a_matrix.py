n,m=map(int,input().split())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    if l==sorted(l) or l==sorted(l,reverse=True):
        count+=1
print(count)    