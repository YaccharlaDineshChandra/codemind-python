n=int(input())
l=list(map(int,input().split()))
b=[]
c=1
for i in l:
    t=set(l)
    t.discard(i)
    for j in t:
        c*=j
    b.append(c)
    c=1
print(*b)    
        