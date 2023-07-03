def is_len(i):
    b=[]
    while i!=0:
        r=i%10
        b.append(r)
        i=i//10
    return len(b)


n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    a=is_len(i)
    c.append(a)
print(c.count(min(c)))    
    
    