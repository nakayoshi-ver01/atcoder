# from collections import defaultdict,deque
# from sortedcontainers import SortedList,SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,x=map(int,input().split())
p=list(map(int,input().split()))
# s=list(input())
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0]=1

for i in range(1,n+1):
    for j in range(n+1):
        dp[i][j]=dp[i-1][j]*(0.01*(100-p[i-1]))+dp[i-1][j-1]*(0.01*(p[i-1]))

f=[0 for _ in range(x+1)]

for i in range(1,x+1):
    temp=0
    for j in range(1,n+1):
        temp+=dp[-1][j]*f[max(0,i-j)]
    f[i]=(1+temp)/(1-dp[-1][0])
print(f[-1])