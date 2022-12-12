n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2==0:
        a.append(i)
for i in a:
    if i not in b:
        b.append(i)
print(len(b))        
        
        
    
    