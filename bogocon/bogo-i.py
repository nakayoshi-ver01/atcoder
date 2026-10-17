# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache
for _ in range(t):
    h,w,k=map(int,input().split())
    grid=[list(input()) for _ in range(h)]
    dots=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]=='.':
                dots+=1
    print(dots)