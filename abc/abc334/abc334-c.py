#n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
if k==1:
    print(0)
elif k%2==0:
    ans=0
    for i in range(k//2):
        ans+=abs(a[i*2]-a[i*2+1])
    print(ans)
else:
    flist=[]
    for i in range(1,k):
        flist.append(a[i]-a[i-1])
    rlist=[]
    for i in range(k-1):
        rlist.append(a[i+1]-a[i])
    flist.sort()
    rlist.sort()
    
    print(min(sum(flist[:k-3]),sum(rlist[:k-3])))