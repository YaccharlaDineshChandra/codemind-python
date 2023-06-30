n,m=map(int,input().split())
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
a=[]
for i in range(1,n-1):
    for j in range(1,m-1):
        a.append(s[i][j])
print(sum(a))        