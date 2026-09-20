from collections import defaultdict
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
# from functools import cmp_to_key, lru_cache

def rec(depth,n):
    for i in edge[n]:
        if i in level:
            if depth%2==level[i]%2 and (depth-level[i]>1):
                print(depth+1-level[i])
                print(*root[level[i]:depth+1])
                return True
        else:
            level[i]=depth+1
            root[depth+1]=i
            ans=rec(depth+1,i)
            if ans:
                return True
            root[depth+1]=-1
    else:
        return False
    


for _ in range(t):
    n,m=map(int,input().split())
    edge=defaultdict(set)

    for i in range(m):
        u,v=map(int,input().split())
        edge[u].add(v)
        edge[v].add(u)
    level=defaultdict(int)
    level[1]=1
    root=[-1 for _ in range(n+1)]
    root[1]=1
    if not rec(1,1):
        print(-1)
    
    