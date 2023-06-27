n=int(input())
l=list(map(int,input().split()))
count1,count2=0,0
for i in l:
    if i%2==0:
        count1+=1
    else:
        count2+=1
print(count1,count2)        