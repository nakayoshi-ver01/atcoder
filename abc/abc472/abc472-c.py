# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

flg=[True for i in range(n)]
now=0
for i in range(n):
    if i>=m:
        if flg[i-m]:
            now-=a[i-m]
    if now+a[i]<=k:
        flg[i]=True
        now+=a[i]
    else:
        flg[i]=False

for i in range(n):
    print('Yes' if flg[i] else 'No')
