n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
while n%2==0:
    n//=2
while n%3==0:
    n//=3
if n==1:
    print('Yes')
else:
    print('No')