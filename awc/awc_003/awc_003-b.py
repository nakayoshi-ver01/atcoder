# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
hands=[list(map(str,input().split())) for _ in range(n)]

ans=0
for i in range(n-1):
    if hands[i][1]==hands[i+1][0]:
        ans+=1
print(ans)