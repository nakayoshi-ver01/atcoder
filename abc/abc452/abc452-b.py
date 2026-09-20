# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[['.' for i in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i==0 or i==h-1 or j==0 or j==w-1:
            grid[i][j]='#'

for i in range(h):
    print(''.join(grid[i]))
    