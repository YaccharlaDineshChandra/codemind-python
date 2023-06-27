n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i not in a:
        a.append(i)
    else:
        b.append(i)
print(*b)        