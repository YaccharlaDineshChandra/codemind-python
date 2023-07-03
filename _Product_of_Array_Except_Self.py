n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=[]
    c=1
    a.append(i)
    for j in l:
        if j not in a:
            c*=j
    b.append(c)
print(*b)            
            
            