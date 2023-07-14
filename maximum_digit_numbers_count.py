n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    a.append(len(str(i)))
for i in range(n):
    if max(a)==a[i]:
        b.append(l[i])
print(*b)        