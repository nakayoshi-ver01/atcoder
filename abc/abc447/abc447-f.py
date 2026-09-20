from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n=int(input())
    dp=[-1 for _ in range(n+1)]
    edges=defaultdict(set)
    start=-1
    for i in range(n-1):
        u,v=map(int,input().split())
        edges[u].add(v)
        edges[v].add(u)
    for i in range(1,n+1):
        if len(edges[i])<3:
            dp[i]=0
        if start==-1 and len(edges[i])==1:
            start=i
    
    state=deque()
    state.append(start)
    af=[True for _ in range(n+1)]
    af[start]=False
    while state:
        now=state.popleft()
        for i in edges[now]:
            if af[i]:
                state.append(i)
                af[i]=False
                if len(edges[i])>=3:
                    dp[i]=max(dp[now]+1,dp[i])
                else:
                    dp[i]=0
    
    print(max(dp))