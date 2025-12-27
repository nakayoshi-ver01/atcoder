# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,x=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

dishes=[list(map(int,input().split())) for _ in range(n)]
left=0
right=n*2*10**5

while left+1<right:
    dp=[[[-1,-1,-1] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0]=[0,0,0]
    center=(left+right)//2
    for i in range(n):
        dish=dishes[i]
        for j in range(x-dish[2]+1):
            if (dp[i][j][dish[0]-1])>: