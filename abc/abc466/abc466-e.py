# from collections import defaultdict,deque
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
# grid=[list(input()) for _ in range(h)]

a_side=[]
b_side=[]
for i in range(n):
    a,b=map(int,input().split())
    a_side.append(a)
    b_side.append(b)

dp=[[-1 for _ in range(2*k+1)]for _ in range(n+1)]

dp[0][0]=0

for i in range(n):
    for j in range(2*k+1):
        if dp[i][j]==-1:
            continue
        if j%2==0:
            dp[i+1][j]=max(dp[i][j]+a_side[i],dp[i+1][j])
            if j!=2*k:
                dp[i+1][j+1]=max(dp[i][j]+b_side[i],dp[i+1][j+1])
        if j%2==1:
            dp[i+1][j]=max(dp[i][j]+b_side[i],dp[i+1][j])
            if j!=2*k:
                dp[i+1][j+1]=max(dp[i][j]+a_side[i],dp[i+1][j+1])
print(max(dp[-1]))