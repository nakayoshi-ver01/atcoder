# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
grid=[list(input()) for _ in range(h)]
mod=10**9+7
pattern=[[0 for _ in range(w)] for _ in range(h)]
pattern[0][0]=1
for i in range(h):
    for j in range(w):
        a=0
        b=0
        if grid[i][j]!='#' and (i,j)!=(0,0):
            if i>0 and grid[i-1][j]=='.':
                a=pattern[i-1][j]
            if j>0 and grid[i][j-1]=='.':
                b=pattern[i][j-1]
            pattern[i][j]=(a+b)%mod

print(pattern[-1][-1])