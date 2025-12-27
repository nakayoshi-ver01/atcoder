n=int(input())
minbig=[-1 for _ in range(n)]
a=list()
for i in range(n):
    p=list(map(int,input().split()))
    a.append(p)
for i in range(n-1):
    if a[i][0]>=a[i+1][1]:
        minbig[i]=a[i][0]
        minbig[i+1]=a[i+1][1]
    if a[i][1]<=a[i+1][0]:
        minbig[i]=a[i][1]
        minbig[i+1]=a[i+1][0]
print(minbig)
ans=minbig
print(minbig[n-1])
for i in reversed(range(1,n)):
    if ans[i]==-1:
        k=[minbig[i-1],a[i][0],a[i][1]]
        k.sort()
        ans[i]=k[1]
    print(ans)