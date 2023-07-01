s=input()
c,d=0,0
for i in s:
    if i=='U':
        c+=1
    elif i=='D':
        c-=1
    elif i=='R':
        d+=1
    else:
        d-=1
if c==0 and d==0:
    print("True")
else:
    print("False")