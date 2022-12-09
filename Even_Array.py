n=int(input())
l=list(map(int,input().split()))
count=0
a=[]
for i in l:
    if i%2==0:
        count=count+1
    a.append(count)
if count==len(l):
    print("True")
else:
    print("False")
        