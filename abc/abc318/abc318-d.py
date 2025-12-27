# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
from functools import lru_cache

weight=[list(map(int,input().split())) for _ in range(n-1)]

@lru_cache(maxsize=10**8)
def dfs(before):
    global n
    global weight
    result=0
    if len(before)==0:
        return 0
    else:
        cand=set(before)
        s=min(cand)
        for t in cand:
            if t!=s:
                tmp=list(cand-{s,t})
                tmp.sort()
                result=max(result,dfs(tuple(tmp))+weight[s][t-s-1])
        return result

if n%2==0:
    test=tuple([i for i in range(n)])
    print(dfs(test))
else:
    result=0
    for i in range(n):
        test=[]
        for j in range(n):
            if i!=j:
                test.append(j)    
        result=max(result,dfs(tuple(test)))
    print(result)