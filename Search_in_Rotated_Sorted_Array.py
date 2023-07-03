n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    if l[i]==k:
        print(i)
        break
else:
    print('-1')