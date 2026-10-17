# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
ok=[i+1 for i in range(n)]
z=[-1 for _ in range(n)]
while 1:
    z=list(map(int,input().split()))
    if all(ok[i]==z[i] for i in range(n)):
        print('ok')
        break
    else:
        print('shuffle')

# n,m=map(int,input().split())
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache