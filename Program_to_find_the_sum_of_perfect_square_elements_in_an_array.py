def is_perfect(i):
    for j in range(i):
        if j*j==i:
            return True
        elif i==1:
            return True




n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if is_perfect(i):
        a.append(i)
print(sum(a))