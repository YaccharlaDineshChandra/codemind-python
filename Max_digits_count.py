n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    a.append(len(str(i)))
print(a.count(max(a)))
    

