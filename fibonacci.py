n=int(input())
a=0
b=1
s=[0,1]
for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    s.append(c)
for i in range(len(s)):
    print(s[i],end=" ")