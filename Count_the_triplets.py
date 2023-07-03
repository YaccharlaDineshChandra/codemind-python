n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    count=0
    for j in l:
        for k in l:
            if j!=k:
                if j+k in l:
                    count+=1
    if count>0:
        print(count//2)
    else:
        print('-1')
    