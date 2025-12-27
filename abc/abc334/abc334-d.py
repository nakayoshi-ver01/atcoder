#n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
a.sort()
rui=[a[0]]
for i in range(1,n):
    rui.append(rui[-1]+a[i])

for i in range(q):
    z=int(input())
    left=0
    right=n-1
    center=(left+right)//2
    while left<right:
        if z<rui[center]:
            right=max(0,center-1)
            center=(left+right)//2
        elif z>rui[center]:
            left=center+1
            center=(left+right)//2
        else:
            break
    if z<rui[center]:
        print(center)
    else:
        print(center+1)