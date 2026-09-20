# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
c=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

now=[0 for _ in range(m)]
for _ in range(n):
    a,b=map(int,input().split())
    now[a-1]+=min(b,c[a-1]-now[a-1])

print(sum(now))