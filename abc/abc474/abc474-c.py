from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

mp=defaultdict(int)

for i in range(n):
    mp[a[i]]=i

for i in range(q):
    q=int(input())
    pos=mp[q]
    a.append(q)
    a[pos]=-1
    mp[q]=len(a)-1

for i in range(len(a)):
    if a[i]!=-1:
        print(a[i],end=' ')
