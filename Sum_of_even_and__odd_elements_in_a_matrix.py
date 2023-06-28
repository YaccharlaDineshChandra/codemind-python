n,m=map(int,input().split())
s=[]
for i in range(n):
    l=list(map(int,input().split()))
    s.append(l)
count1,count2=0,0    
for i in range(n):
    for j in range(m):
        if s[i][j]%2==0:
            count1+=s[i][j]
        else:
            count2+=s[i][j]
print(count1,count2,end=' ')            