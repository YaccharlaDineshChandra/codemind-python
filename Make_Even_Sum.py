n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c+=i
if c%2==0:
    print('1')
else:
    print('0')