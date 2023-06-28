n,m=map(int,input().split())
c1=0
s=[]
s1=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
for j in range(m):
    for i in range(n):
        c1+=s[i][j]
    s1.append(c1)
    c1=0
print(*s1)        
        