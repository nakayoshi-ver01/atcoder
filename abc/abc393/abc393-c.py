from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
edge=defaultdict(set)
ans=0
for _ in range(m):
    a=list(map(int,input().split()))
    if a[0]==a[1]:
        ans+=1
        continue
    if a[1] in edge[a[0]]:
        ans+=1
        continue
    edge[a[0]].add(a[1])
    edge[a[1]].add(a[0])

print(ans)