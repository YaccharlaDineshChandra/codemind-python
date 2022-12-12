n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
d=0
for i in l:
    if i<a or i>b:
        d=d+i
for i in l:
    c=c+i
print(c-d)    



