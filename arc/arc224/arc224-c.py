from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(u,depth):
    nums[u]=depth
    counter=0
    for i in edges[u]:
        if nums[i]==-1:
            rec(i,depth+1)
            counter+=1
for _ in range(t):
    n,m=map(int,input().split())
    nums=[-1 for _ in range(n)]
    edges=defaultdict(set)
    for _ in range(m):
        u,v=map(int,input().split())
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    rec(0,0)
    print(*nums)