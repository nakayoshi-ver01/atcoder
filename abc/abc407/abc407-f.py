# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n=int(input())
    a=list()
    for i in range(2*n):
        a.append(int(input()))
    dp=[0 for _ in range(n+1)]
    for i in range(2*n):
        if i==0:
            dp[1]=a[i]
        elif i%2==1:
            for j in range(1,n+1,2):
                x=dp[j]
                dp[j-1]=max(dp[j],dp[j-1])
                if j+1<n+1:
                    dp[j+1]=max(dp[j]+a[i],dp[j+1])
                dp[j]=0
        else:
            for j in range(0,n+1,2):
                x=dp[j]
                if j-1>=0:
                    dp[j-1]=max(dp[j-1],dp[j])
                if j+1<n+1:
                    dp[j+1]=max(dp[j]+a[i],dp[j+1])
                dp[j]=0
    print(dp[0])