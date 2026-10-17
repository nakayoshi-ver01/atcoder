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
s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

combo=0
tmp=0
for i in range(n):
    if s[i]=='R':
        tmp+=1
    else:
        tmp=0
    combo=max(combo,tmp)
print(combo)