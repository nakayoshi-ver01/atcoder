from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(n)]
# from functools import cmp_to_key, lru_cache

# とりあえず位置記録
nests=dict()
slimes=defaultdict(set)

for i in range(n):
    for j in range(n):
        if grid[i][j].isupper():
            nests[grid[i][j]]=(i,j)
            grid[i][j]='.'
        elif grid[i][j].islower():
            slimes[grid[i][j].upper()].add(i,j)
            grid[i][j]='.'

dirs={'D':[1,0],'R':[0,1],'U':[-1,0],'L':[0,-1]}
