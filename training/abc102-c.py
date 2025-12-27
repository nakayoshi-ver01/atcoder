# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for i in range(n):
    a[i]-=i+1

a.sort()
ans=0
if n%2==1:
    b=a[n//2]
    for i in a:
        ans+=abs(i-b)
    print(ans)
else:
    if (a[n//2-1]+a[n//2])%2==0:
        b=(a[n//2-1]+a[n//2])//2
        for i in a:
            ans+=abs(i-b)
        print(ans)
    else:
        b1=(a[n//2-1]+a[n//2])//2
        ans1=0
        for i in a:
            ans1+=abs(i-b1)
        b2=(a[n//2-1]+a[n//2])//2+1
        ans2=0
        for i in a:
            ans2+=abs(i-b2)
        print(min(ans1,ans2))