#n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
flg=1
for i in range(0,101):
    a.append(i)
    a.sort()
    if sum(a[1:n-1])>=m:
        print(i)
        flg=0
        break
    a.remove(i)
if flg==1:
    print(-1)