#n=int(input())
n,m,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()

rui=[0]
cost=0
for i in range(m):
    rui.append(rui[-1]+b[i])
#0の場合を作っとくべきだった
for i in range(n):
    left=0
    right=m
    center=(left+right)//2
    while left+1<=right:
        center=(left+right)//2
        if b[center]+a[i]>p:
            right=center
        else:
            left=center
    if a[i]+b[center]<=p:
        cost+=(rui[center]+a[i]*(center)+p*(m-center))
    else:
        cost+=(rui[center]+a[i]*(center)+p*(m-center))
    print(center)     
print(cost)