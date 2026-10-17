# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,v=map(int,input().split())
w=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i+j+k+3<=v:
                ans=max(ans,w[i]+w[k]+w[j])

print(ans)