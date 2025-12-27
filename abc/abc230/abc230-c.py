# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[['.' for _ in range(s-r+1)] for _ in range(q-p+1)]



for i in range(q-p+1):
    for j in range(s-r+1):
        if (p+i)+(r+j)==a+b:
            grid[i][j]='#'
        elif a-b==(p+i)-(r+j):
            grid[i][j]='#'

for i in grid:
    print(''.join(i))
