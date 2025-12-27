# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[['#' for _ in range(n)] for _ in range(n)]

for i in range(n//2):
    k=i*2+1
    for j in range(k,n-k):
        grid[k][j]='.'
        grid[n-k-1][j]='.'
        grid[j][k]='.'
        grid[j][n-k-1]='.'
for i in grid:
    print(''.join(i))