n=list(input())
a=[]
for i in n:
    if i in 'aeiouAEIOU' and i not in a:
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print(-1)
    