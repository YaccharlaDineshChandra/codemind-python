n=int(input())
l=list(map(int,input().split()))
c=[]
count=0
for i in l:
    if i%2!=0:
        if i not in c:
            c.append(i)
print(len(c))            
            