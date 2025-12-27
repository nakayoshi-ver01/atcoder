from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

edge=defaultdict(set)
for i in range(m):
    a,b=map(int,input().split())
    edge[a].add(b)


visited=[True for _ in range(n+1)]
waiting=deque()
waiting.append((1,0))
while waiting:
    now=waiting.popleft()
    if now[0]==1 and now[1]>0:
        print(now[1])
        break
    for i in edge[now[0]]:
        if visited[i]:
            visited[i]=False
            waiting.append((i,now[1]+1))
else:
    print(-1)