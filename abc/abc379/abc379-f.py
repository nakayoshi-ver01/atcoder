# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

import bisect
n,m=map(int,input().split())
a = list(map(int,input().split()))
length = [10**10 for _ in range(n+1)]
length[0]=0
dp = [0 for _ in range(n+1)]

for i in range(n):
    x = bisect.bisect_left(length, a[i])
    dp[i] = dp[x] + 1
    length[dp[i]] = min(length[dp[i]],a[i])

print(length,dp)