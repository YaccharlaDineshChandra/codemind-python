import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
s1=s*(s-a)*(s-b)*(s-c)
ar=float((s1)**0.5)
print("%.2f"%ar)