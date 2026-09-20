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
# s=list(input())
# grid=[list(input()) for _ in range(h)]

a=[tuple(map(int,input().split())) for _ in range(n)]

a.sort()

min_y=n+1
ans=0
for i in a:
    if min_y>i[1]:
        ans+=1
        min_y=i[1]

print(ans)