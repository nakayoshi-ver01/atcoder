# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
from functools import lru_cache
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


dp=[0 for _ in range(n+1)]
dp[1]=1

for i in range(1,n+1):
    for j in range(k):
        if a[j]>i:
            break
        else:
            dp[i]=max(dp[i],a[j]+((i-a[j])-dp[i-a[j]]))
print(dp[-1])