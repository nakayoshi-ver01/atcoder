# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

dp=[[0,0] for _ in range(n)]

dp[0][0]=m

for i in range(1,n):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=(dp[i-1][0]*(m-1)+dp[i-1][1]*(m-2))%998244353

print(dp[-1][1])