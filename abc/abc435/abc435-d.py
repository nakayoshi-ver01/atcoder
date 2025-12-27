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

edge=defaultdict(set)
black_node=[False for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    edge[y].add(x)

q=int(input())
for _ in range(q):
    order,v=map(int,input().split())
    if order==1:
        if not black_node[v]:
            state=deque()
            state.append(v)
            black_node[v] = True
            while state:
                now = state.popleft()
                for i in edge[now]:
                    if not black_node[i]:
                        black_node[i] = True
                        state.append(i)
    if order==2:
        print('Yes' if black_node[v] else 'No')