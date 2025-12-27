
n=int(input())
#n,m=map(int,input().split())
a=list(map(int,input().split()))
#s=list(input())
if a.count(a[0])==n:
    print('Yes')
else:
    print('No')