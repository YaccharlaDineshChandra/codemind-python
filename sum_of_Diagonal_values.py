n,m=map(int,input().split())
s=[]
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
for i in range(n):
    for j in range(m):
        if i==j:
            a.append(s[i][j])
        elif i+j==m-1:
            a.append(s[i][j])
print(sum(a))                