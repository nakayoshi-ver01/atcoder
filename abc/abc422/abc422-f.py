from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,m=map(int,input().split())
w=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
edge=defaultdict(set)

for _ in range(m):
    u,v=map(int,input().split())
    edge[u].add(v)
    edge[v].add(u)


state=[]
ans=[10**15 for _ in range(n+1)]


# 消費済み、コスト、現在地
heapq.heappush(state,(0,0,1))

while state:
    now=heapq.heappop(state)
    if ans[now[2]]==10**15:
        ans[now[2]]=now[0]
        for i in edge[now[2]]:
            if ans[i]==10**15:
                heapq.heappush(state,(now[0]+now[1]+w[now[2]-1],now[1]+w[now[2]-1],i))

for i in range(1,n+1):
    print(ans[i])