# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

p=[set() for _ in range(n)]

ans=list()
for i in range(k):
    log=list(map(int,input().split()))
    p[log[0]-1].add(log[1])
    if len(p[log[0]-1])==m:
        ans.append(log[0])

print(*ans)