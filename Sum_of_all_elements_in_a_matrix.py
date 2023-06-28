n,m=map(int,input().split())
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    a=sum(l)
    s.append(a)
print(sum(s))    
        