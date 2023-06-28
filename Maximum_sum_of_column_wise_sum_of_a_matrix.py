n,m=map(int,input().split())
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
s1=[]
count=0
for j in range(m):
    for i in range(n):
        count+=s[i][j]
    s1.append(count)
    count=0
print(max(s1))