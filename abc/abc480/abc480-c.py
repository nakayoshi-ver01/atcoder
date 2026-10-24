# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,k,t=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

a.sort()

now=0
ans=0
for i in range(n):
    time=min(t,a[i])-now
    if time>0:
        count=time//k+min(time%k,1)
        ans+=count
        now=max(a[i]+k,now+k*count)
    else:
        now=max(now,a[i]+k)
    if now>t:
        break
else:
    time=t-now
    if time>0:
        count=time//k+min(time%k,1)
        ans+=count
        now=t
print(ans)