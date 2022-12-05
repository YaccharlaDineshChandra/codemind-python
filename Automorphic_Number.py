n=int(input())
t=n
c=1
a=n*n
while n!=0:
    c=c*10
    n=n//10
if a%c==t:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
    
