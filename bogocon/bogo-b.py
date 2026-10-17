# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in reversed(range(1,n-1)):
        if a[i]>=a[i+1]:
            ans+=a[i]-a[i+1]
            a[i]-=a[i]-a[i+1]
    if a[0]<=a[1]:
        print(ans)
    else:
        print(-1)
        
# n,m=map(int,input().split())
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache