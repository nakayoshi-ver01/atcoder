# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

trees=list()
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        heapq.heappush(trees,query[1])
    if query[0]==2:
        while trees:
            shortest=heapq.heappop(trees)
            if shortest>query[1]:
                heapq.heappush(trees,shortest)
                break
    print(len(trees))

