a=input()
b=int(a[::-1])
sum=0
i=1
while b:
    sum=sum+(b%10)**i
    b=b//10
    i=i+1
if int(a)==sum:
    print(True)
else:
    print(False)
    