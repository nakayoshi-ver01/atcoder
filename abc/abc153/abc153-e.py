# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,n=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

magics=[]
for _ in range(n):
    magic=list(map(int,input().split()))
    magics.append(magic)

dp=[[10**10 for _ in range(h+1)] for _ in range(n+1)]
dp[0][h]=0

for i in range(n):
    magic=magics[i]
    for j in reversed(range(h+1)):
        dp[i+1][j]=min(dp[i][j],dp[i+1][j])
        dp[i][max(0,j-magic[0])]=min(dp[i][max(0,j-magic[0])],dp[i][j]+magic[1])
       

print(dp[-1][0])