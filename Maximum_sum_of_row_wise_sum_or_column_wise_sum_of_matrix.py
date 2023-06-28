n,m=map(int,input().split())
c=[]
for i in range(n):
    l=list(map(int,input().split()))
    c.append(sum(l))
print(max(c))