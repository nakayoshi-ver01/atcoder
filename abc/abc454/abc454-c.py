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

cand=[False for _ in range(n)]
edge=defaultdict(set)

for _ in range(m):
    a,b=map(int,input().split())
    edge[a-1].add(b-1)

state=deque()
state.append(0)
cand[0]=True
while state:
    now=state.popleft()
    for i in edge[now]:
        if not cand[i]:
            cand[i]=True
            state.append(i)

print(cand.count(True))