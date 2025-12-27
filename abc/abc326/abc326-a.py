# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
if n-m>0 and abs(n-m)<=3:
    print('Yes')
elif n-m<=0 and abs(n-m)<=2:
    print('Yes')
else:
    print('No')