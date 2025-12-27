#n=int(input())
n,m=map(int,input().split())
#a=list(map(int,input().split()))
#s=list(input())
if n%m==0:
    print(n//m)
else:
    print(n//m+1)