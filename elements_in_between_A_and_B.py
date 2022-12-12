n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
e=[]
for i in l:
    e.append(i)
for i in e:
    if i<a or i>b:
        c.append(i)
for i in e:
    if i not in c:
        d.append(i)
if len(d)==0:
    print('-1')
else:
    print(*d)
    
    
    