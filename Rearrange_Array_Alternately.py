n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    c=l[::-1]
    b=[]
    for j in range(len(l)):
        if c[j]>l[j]:
            b.append(c[j])
            b.append(l[j])
    for i in l:
        if i not in b:
            b.append(i)
    print(*b)       