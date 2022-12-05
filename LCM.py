a,b=map(int,input().split())
if a>b:
    gr=a
else:
    gr=b
while(True):
    if gr%a==0 and gr%b==0:
        print(gr)
        break
    gr+=1