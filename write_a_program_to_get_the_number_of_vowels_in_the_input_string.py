n=input()
c=0
for i in n:
    if i in 'AEIOUaeiou':
        c+=1
if c>0:
    print(c)
else:
    print('0')