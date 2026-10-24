# 事前準備したモジュールは以下のサイトに公開済み
# https://atcoder.jp/contests/abc100/submissions/80089964

from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,s,t=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

edge=defaultdict(set)
for _ in range(m):
    a,b=map(int,input().split())
    edge[a-1].add(b-1)

for i in edge:
    edge[i]=list(edge[i])
    edge[i].sort()

s-=1
t-=1

INF=10**10
cost=[INF for _ in range(n)]
state=deque()
state.append((s,0))

while state:
    now=state.popleft()
    if cost[now[0]]==INF:
        cost[now[0]]=min(now[1],cost[now[0]])
        for i in range(len(edge[now[0]])):
            if i==0:
                if cost[edge[now[0]][i]]==INF:
                    state.appendleft((edge[now[0]][i],now[1]))
            else:
                if cost[edge[now[0]][i]]==INF:
                    state.append((edge[now[0]][i],now[1]+1))

if cost[t]==INF:
    print(-1)
else:
    print(cost[t])