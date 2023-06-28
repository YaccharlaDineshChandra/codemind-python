n,m=map(int,input().split())
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
c=[]
d=[]
for i in range(n):
    if i%2==0:
        a=sum(s[i])
        c.append(a)
    else:
        b=sum(s[i])
        d.append(b)
print(sum(c),sum(d),end=' ')        
    