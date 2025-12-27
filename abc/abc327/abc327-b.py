n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
flg=0
k=1
while k**k<=n:
    if k**k==n:
        flg=1
        break
    else:
        k+=1
if flg:
    print(k)
else:
    print(-1)