n=int(input())
while n>9:
    res=0
    while n:
        r=n%10
        res=res+r*r
        n=n//10
    n=res    
if res==1:
    print("True")
else:
    print("False")