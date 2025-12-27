from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# import math
# import bisect
from functools import lru_cache
import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

sys.setrecursionlimit(10**9)
edge=defaultdict(set)
for i in range(m):
    a,b,w=map(int,input().split())
    edge[a].add((b,w,i))

ans=2**10

@lru_cache
def dfs(path,now):
    global ans
    global edge
    global n
    if now[0]==n:
        ans=min(ans,now[1])
    for i in edge[now[0]]:
        if i[2] not in set(path):
            dfs(tuple(set(path)|{i[2]}),(i[0],now[1]^i[1]))
    return


dfs(tuple(),(1,0))
print(ans if ans!=1024 else -1)