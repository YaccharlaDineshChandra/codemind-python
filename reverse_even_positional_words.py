n=input().split(' ')
a=[]
for i in range(len(n)):
    if i%2==0:
        a.append(n[i][::-1])
    else:
        a.append(n[i])
print(*a)    