from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
w-=1
rooms=defaultdict(list)
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    b-=1
    if b==0 or b==w:
        continue
    rooms[a].append(b)

ans=0
floors=list(rooms.keys())
floors.sort()
dp=[[0,0] for _ in range(len(floors)+1)]
dp[0][1]=10**20
for i in range(len(floors)):
    if len(rooms[floors[i]])>1:
        rooms[floors[i]].sort()
        min_cost=10**10
        for j in range(len(rooms[floors[i]])-1):
            cost=(rooms[floors[i]][j])*2+(w-rooms[floors[i]][j+1])*2
            min_cost=min(min_cost,cost)
        dp[i+1][0]=min(dp[i][0]+min_cost,dp[i][1]+w)
        dp[i+1][1]=min(dp[i][1]+min_cost,dp[i][0]+w)
    else:
        cost=min((rooms[floors[i]][0])*2,(w-rooms[floors[i]][0])*2)
        dp[i+1][0]=min(dp[i][0]+(rooms[floors[i]][0])*2,dp[i][1]+w)
        dp[i+1][1]=min(dp[i][1]+(w-rooms[floors[i]][0])*2,dp[i][0]+w)
    
print(min(dp[-1][0],dp[-1][1]+w))