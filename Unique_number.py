n=int(input())
a=str(n)
l=[]
while n!=0:
    v=n%10
    l.append(v)
    n=int(n/10)
for i in l:
    if l.count(i)>1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')
    