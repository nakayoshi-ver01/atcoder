# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
h=2
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


for i in range(2):
    for j in range(2):
        if grid[i][j]=='A':
            a=(i,j)
        elif grid[i][j]=='D':
            d=(i,j)


if a[0]==d[0] or a[1]==d[1]:
    print('Yes')
else:
    print('No')