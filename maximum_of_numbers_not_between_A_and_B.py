n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in range(a,b+1):
    d.append(i)
for i in l:
    if i not in d:
        c.append(i)
if len(c)==0:
    print('-1')
else:
    print(max(c))
