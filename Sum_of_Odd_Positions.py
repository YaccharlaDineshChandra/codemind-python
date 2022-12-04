n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if i%2!=0:
        count+=l[i]
print(count)        
        