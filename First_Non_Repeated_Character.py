n=int(input())
for i in range(n):
    a=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print('-1')