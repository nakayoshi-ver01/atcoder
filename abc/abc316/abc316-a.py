#n=int(input())
n,h,x=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
for i in range(n):
    if h+a[i]>=x:
        print(i+1)
        break