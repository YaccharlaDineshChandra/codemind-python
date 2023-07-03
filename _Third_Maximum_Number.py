n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=list(l)
l.sort()
l=list(l)
if len(l)>2:
    l.remove(max(l))
    l.remove(max(l))
    print(max(l))
else:
    print(max(l))
    


    

    