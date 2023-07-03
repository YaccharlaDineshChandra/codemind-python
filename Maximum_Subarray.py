n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    c=0
    for j in range(i,n):
        c+=l[j]
        s.append(c)
print(max(s))        
        