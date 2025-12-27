from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    h,w=map(int,input().split())
    grid=[list(input()) for _ in range(h)]
    dp=[[1000 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(h+1):
        dp[i][0]=0
    for i in range(w+1):
        dp[0][i]=0
    for i in range(h):
        for j in range(w):
            if i==0:
                if grid[i][j]=='.':
                    dp[i+1][j+1]=0
                else:
                    dp[i+1][j+1]=1
            elif j==0:
                if grid[i][j]=='.':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i][j+2])
                else:
                    if grid[i-1][j]=='#' and grid[i-1][j+1]=='#' and grid[i][j+1]=='#':
                        dp[i+1][j+1]=min(dp[i][j+1],dp[i][j+2])+1
                    else:
                        dp[i+1][j+1]=min(dp[i][j+1],dp[i][j])
            elif j==w-1:
                if grid[i][j]=='.':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i][j])
                else:
                    if grid[i-1][j]=='#' and grid[i-1][j-1]=='#' and grid[i][j-1]=='#':
                        dp[i+1][j+1]=min(dp[i][j-1],dp[i][j])+1,dp[i+1][j+1]
                    else:
                        dp[i+1][j+1]=min(dp[i][j-1],dp[i][j])
            
            else:
                if grid[i][j]=='.':
                    dp[i+1][j+1]=0
                else:
                    if 
                    dp[i+1][j+1]=max((dp[i][j]-1,dp[i+1][j]-1,dp[i][j+1]-1))+1
        print(dp[i+1])