from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edges=defaultdict(set)
costs=defaultdict(int)

for i in range(n-1):
    u,v,w=map(int,input().split())
    edges[u].add(v)
    edges[v].add(u)
    costs[(u,v)]=w
    costs[(v,u)]=w

leafs=set()
for i in range(1,n+1):
    if len(edges[i])==1:
        leafs.add(i)


states=list()
for i in leafs:
    heapq.heappush(states, (costs[(*edges[i],i)]*abs(a[i-1]),i))
# print(states)
ans=0
bf=[True for i in range(n+1)]
while states:
    current=heapq.heappop(states)
    now=current[1]
    if len(edges[now])>0 and bf[now]==True:
        bf[now]=False
        via=edges[now].pop()
        ans+=abs(a[now-1])*costs[(via,now)]
        a[via-1]+=a[now-1]
        a[now-1]=0
        edges[via].remove(now)
        if len(edges[via])==1 and bf[via]==True:
            heapq.heappush(states, (costs[(*edges[via],via)]*abs(a[via-1]),via))
    # print(ans,now,states)
print(ans)