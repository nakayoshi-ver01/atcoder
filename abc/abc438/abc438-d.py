# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

dp=[[0,0,0] for _ in range(n+1)]
for i in range(n):
    dp[i+1][0]=dp[i][0]+a[i]
    if i>0:
        dp[i+1][1]=max(dp[i][0],dp[i][1])+b[i]
    if i>1:
        dp[i+1][2]=max(dp[i][1],dp[i][2])+c[i]
print(dp[-1][-1])