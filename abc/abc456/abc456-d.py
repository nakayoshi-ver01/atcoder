# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

length=len(s)
dp=[[0,0,0,0] for _ in range(length+1)]
dp[0][0]=1


mod=998244353
for i in range(length):
    if s[i]=='a':
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=sum(dp[i])
        dp[i+1][2]=dp[i][2]
        dp[i+1][3]=dp[i][3]
    elif s[i]=='b':
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]
        dp[i+1][2]=sum(dp[i])
        dp[i+1][3]=dp[i][3]
    elif s[i]=='c':
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]
        dp[i+1][2]=dp[i][2]
        dp[i+1][3]=sum(dp[i])
    for j in range(4):
        dp[i+1][j]%=mod

print((sum(dp[-1])-1)%mod)