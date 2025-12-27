m=int(input())
#n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
total=sum(a)
k=total//2+1
now=0
for i in range(m):
    if now+a[i]<k:
        now+=a[i]
    else:
        print(i+1,k-now)
        break