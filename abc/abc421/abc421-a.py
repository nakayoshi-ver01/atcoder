# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# a=list(map(int,input().split()))
# s=list(input())
grid=[input() for _ in range(n)]

x,y=map(str,input().split())

if grid[int(x)-1]==y:
    print('Yes')
else:
    print('No')