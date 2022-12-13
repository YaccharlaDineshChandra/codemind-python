n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if i not in a and l.count(i)==k:
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print('-1')