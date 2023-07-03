n,k=map(int,input().split())
l=list(map(int,input().split()))
a,b,c=0,0,0
for i in range (len(l)):
    if l[i]==k:
        c+=1
for i in range(len(l)):
    a=0
    a+=l[i]
    for j in range(i+1,n):
        a+=l[j]
        if a==k:
            c+=1
print(c)            
        
        
    