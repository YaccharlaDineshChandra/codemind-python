s=input().split()
a=[]
for i in s:
    c=0
    l=list(i)
    for i in l:
        if i in 'aeiou':
            c+=1
    a.append(c)
print(*a)   