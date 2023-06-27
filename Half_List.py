n=int(input())
l=list(map(int,input().split()))
s1=[]
a=l[len(l)//2:]
b=l[:len(l)//2]
a.reverse()
s2=a+b
print(*s2)

