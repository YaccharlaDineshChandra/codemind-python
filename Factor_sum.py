def fac(i):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=j
    return c

l=list(map(int,input().split(',')))
b=[]
for i in l:
    a=fac(i)
    if a in l:
        b.append(i)
d=sorted(b)        
if len(d)>0:
    print(*d)
else:
    print('-1')
        