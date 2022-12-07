n=int(input())
l=list(map(int,input().split()))
count=0
a=sum(l)
b=len(l)
c=a//b
for i in l:
    if i>=c:
        count=count+1
print(count)        