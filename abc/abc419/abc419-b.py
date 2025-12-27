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

hq=list()

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        heapq.heappush(hq,query[1])
    else:
        print(heapq.heappop(hq))
