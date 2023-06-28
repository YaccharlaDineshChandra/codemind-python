n,m=map(int,input().split())
c1=[]
for i in range(n):
    l=list(map(int,input().split()))
    c1.append(sum(l))
print(*c1)    
    