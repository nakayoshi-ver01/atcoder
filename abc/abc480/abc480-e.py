# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

g=[1,1]
for i in range(3,20):
    
    for j in range(1,int(n**(1/i))+1):
        ok=0
        ng=n
        while ng-ok>1:
            center=ng-ok
            if j