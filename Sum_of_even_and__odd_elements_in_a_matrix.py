n,m=map(int,input().split())
c1,c2=0,0
for i in range(n):
    l=list(map(int,input().split()))
    for j in l:
        if j%2==0:
            c1+=j
        else:
            c2+=j
print(c1,c2,end=' ')    