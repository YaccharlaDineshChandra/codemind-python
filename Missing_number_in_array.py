n=int(input())
for i in range(n):
    a=int(input())
    l1=list(map(int,input().split()))
    l2=[]
    for i in range(1,a+1):
        l2.append(i)
    for j in l2:
        if j not in l1:
            print(j)
        
    