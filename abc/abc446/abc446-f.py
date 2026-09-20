from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edges=defaultdict(set)

can=[True]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    if a!=b:
        edges[a].add(b)
    if a>b:
        can[b]=False

ans=[-1 for _ in range(n+1)]
reachable=[False]*(n+1)
state=deque()
state.append(1)
reachable[1]=True
while state:
    now=state.popleft()
    for i in edges[now]:
        if not reachable[i] and can[i]:
            reachable[i]=True
            state.append(i)

max_v=1
while max_v<=n and reachable[max_v]:
    max_v+=1

for i in range(1,max_v):
    