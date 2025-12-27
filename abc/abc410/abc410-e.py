# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,h,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

monsters=[]
for _ in range(n):
    monsters.append(tuple(map(int,input().split())))

dp=[[-1 for _ in range(h+1)] for _ in range(n+1)]

dp[0][0]=m

for i in range(n):
    for j in range(h+1):
        if dp[i][j]!=-1:
            if monsters[i][0]+j<=h:
                dp[i+1][j+monsters[i][0]]=max(dp[i][j],dp[i+1][j+monsters[i][0]])
            if monsters[i][1]<=dp[i][j]:
                dp[i+1][j]=max(dp[i][j]-monsters[i][1],dp[i+1][j])

ans=0
for i in range(n+1):
    if max(dp[i])>-1:
        ans=i

print(ans)