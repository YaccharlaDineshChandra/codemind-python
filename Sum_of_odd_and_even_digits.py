n=int(input())
l=list(map(int,input().split()))
c1,c2=0,0
for i in range(n):
    if i%2==0:
        c1+=l[i]
    else:
        c2+=l[i]
if(abs(c1-c2))==0:
    print("YES")
else:
    print("NO")
    