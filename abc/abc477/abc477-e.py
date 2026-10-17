from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

center_dist=dict()
dijkstra=[]
heapq.heappush(dijkstra,(0,n))
center_dist[n]=0
while dijkstra:
    now=heapq.heappop(dijkstra)
    if now[1] not in center_dist:
        center_dist[now[1]]=now[0]
    if now[1]==n:
        for i in range(n):
            heapq.heappush(dijkstra,(b[i],i))
    else:
        if (now[1]+1)%n not in center_dist:
            heapq.heappush(dijkstra,(now[0]+a[(now[1])%n],(now[1]+1)%n))
        if (now[1]-1)%n not in center_dist:
            heapq.heappush(dijkstra,(now[0]+a[(now[1]-1)%n],(now[1]-1)%n))


acc=[0]
for i in range(n):
    acc.append(acc[-1]+a[i])
for _ in range(q):
    s,t=map(int,input().split())
    if max(s,t)!=n+1:
        roop=min(acc[max(s,t)-1]-acc[min(s,t)-1],acc[-1]-(acc[max(s,t)-1]-acc[min(s,t)-1]))
        use_center=center_dist[s-1]+center_dist[t-1]
        print(min(roop,use_center))
    else:
        print(center_dist[min(s,t)-1])