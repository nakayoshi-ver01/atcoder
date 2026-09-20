from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

colors=defaultdict(int)
for i in a:
    colors[i]+=1


ans=10**10
for i in colors:
    ans=min(ans,n-colors[i])
print(ans)