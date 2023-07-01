a=int(input())
l=list(map(int,input().split()))
c=0
d=[]
for i in l:
    if i == 1:
        c+=1
        d.append(c)
    else:
        c=0
if len(d)!=0:
    print(max(d))
else:
    print('0')