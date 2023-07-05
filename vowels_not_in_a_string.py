s=list(input())
c=[]
for i in 'aeiou':
    if i not in s:
        c.append(i)
if len(c)>0:
    print(*c)
else:
    print('0')