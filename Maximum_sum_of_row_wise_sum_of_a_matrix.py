n,m=map(int,input().split())
m=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(sum(l))
print(max(m))    