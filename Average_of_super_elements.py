n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a and l.count(i)==i:
        a.append(i)
if len(a)>0:
    print("{:.2f}".format(sum(a)/len(a)))
else:
    print('-1')