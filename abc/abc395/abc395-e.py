from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
n,m,x=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
z=10**6
edge=defaultdict(set)
for i in range(n):
    edge[i+1].add((i+1+n,x))
    edge[i+1+n].add((i+1,x))
for i in range(m):
    u,v=map(int,input().split())
    edge[u].add((v,1))
    edge[v+n].add((u+n,1))

state=[]
# 現コスト、現在地、flg
heapq.heappush(state,(0,1))
flg = [True for _ in range(2*n+1)]
while state:
    now=heapq.heappop(state)
    if now[1]%n==0:
        print(now[0])
        break
    if flg[now[1]]:
        flg[now[1]]=False
        for i in edge[now[1]]:
            if flg[i[0]]:
                heapq.heappush(state,(now[0]+i[1],i[0]))
