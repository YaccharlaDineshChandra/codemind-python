n=int(input())
l=[]
for i in range(n):
    d=int(input())
    l.append(d)
m=int(input())
c=0
for i in l:
    if i<=m:
        c+=1
    else:
        c+=2
print(c)        