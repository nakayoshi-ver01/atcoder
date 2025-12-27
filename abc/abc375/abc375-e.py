from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())

# s=list(input())
player=defaultdict(list)
total=0
for i in range(n):
    a=list(map(int,input().split()))
    player[a[0]].append(a[1])
    total+=a[1]


if total%3!=0:
    print(-1)
else:
    dp=[[[100 for _ in range(total//3+1)]for _ in range(total//3+1)]for _ in range(n+1)]
    dp[0][0][0]=0
    counter=0

    player[1].sort()
    for j in player[1]:
        counter+=1
        for k in range(total//3+1-j):
            for i in range(total//3+1):
                dp[counter][k+j][i]=min(dp[counter-1][k][i],dp[counter][k+j][i])
        for k in range(total//3+1):
            for i in range(total//3+1-j):
                dp[counter][k][i+j]=min(dp[counter-1][k][i]+1,dp[counter][k][i+j])
        print(dp[counter])
        print(counter)
    player[2].sort()
    for j in player[2]:
        counter+=1
        for k in range(total//3+1-j):
            for i in range(total//3+1):
                dp[counter][k+j][i]=min(dp[counter-1][k][i]+1,dp[counter][k+j][i])
        for k in range(total//3+1):
            for i in range(total//3+1-j):
                dp[counter][k][i+j]=min(dp[counter-1][k][i],dp[counter][k][i+j])
        print(dp[counter])
        print(counter)

    for j in player[3]:
        counter+=1
        for k in range(total//3+1-j):
            for i in range(total//3+1):
                dp[counter][k+j][i]=min(dp[counter-1][k][i]+1,dp[counter][k+j][i])
        for k in range(total//3+1):
            for i in range(total//3+1-j):
                dp[counter][k][i+j]=min(dp[counter-1][k][i]+1,dp[counter][k][i+j])
        print(dp[counter])
        print(counter)
