from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edge=defaultdict(set)
for i in range(m):
    u,v=map(int,input().split())
    edge[u].add(v)
    edge[v].add(u)

limit_edge=defaultdict(set)
for i in edge:
    for j in edge[i]:
        if i<j:
            limit_edge[i].add(j)
print(edge)
print(limit_edge)

bf=[True for _ in range(n+1)]

bf[0]=False
bf[1]=False
state=deque()
state.append(1)
while state:
    now=state.popleft()
    for i in edge[now]:
        if bf[i]:
            bf[i]=False
            state.append(i)

print(bf)
for i in range(n+1):
    if bf[i]:
        mex=i
        break
else:
    mex=i
ans=[-1 for _ in range(n+1)]
cut=edge[1]
ans[1]=len(cut)
af={1}
new_state=list()
heapq.heappush(new_state,1)
while new_state:
    now=heapq.heappop(new_state)
    for i in limit_edge[now]:
        if ans[i]==-1:
            heapq.heappush(new_state,i)
            cut=cut|limit_edge[i]-{i}
            ans[i]=len(cut)
        print(cut,i)
print(ans)