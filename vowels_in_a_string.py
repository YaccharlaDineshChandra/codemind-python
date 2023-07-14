n=list(input())
k=input()
a=0
for i in n:
    if i==k:
        a=n.index(i)
        break
if a>0:
    print('True')
    print(a)
else:
    print('False')
    