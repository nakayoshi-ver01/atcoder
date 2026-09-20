# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

for i in range(n):
    a[i]-=1

for i in range(n//10+1):
    b=a[i*10:i*10+10]
    if any(j//10!=i for j in b):
        print('No')
        break
else:
    print('Yes')