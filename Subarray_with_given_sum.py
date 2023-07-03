n=int(input())
for i in range(n):
    m,p=map(int,input().split())
    l=list(map(int,input().split()))
    a=[]
    for j in range(m):
        s=0
        for k in range(j,m):
            s+=l[k]
            if s==p:
                a.append((j+1,k+1))
                break
    if len(a)>0:
        print(*a[0])
    else:
        print('-1')
                
