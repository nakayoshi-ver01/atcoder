# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
from functools import lru_cache
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

@lru_cache
def dfs(n):
    if n==1:
        return 1
    else:
        return 1+2*dfs(n//2)

print(dfs(int(input())))