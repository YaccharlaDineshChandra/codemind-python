def sum(n):
    if(n<10):
        return n
    res=0
    while n>0:
        r=n%10
        res=res+r
        n=n//10
    return sum(res)   

n=int(input())
print(sum(n))
            