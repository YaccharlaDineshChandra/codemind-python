n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i!=0 and i!=1:
        a.append(i)
if len(a)==0:
    print('True')
else:
    print('False')