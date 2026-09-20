# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        print(query[1]*w)
        h-=query[1]
    elif query[0]==2:
        print(query[1]*h)
        w-=query[1]

