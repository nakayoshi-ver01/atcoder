# from collections import defaultdict,deque
# from sortedcontainers import SortedLibase, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())

base=[i for i in range(n)]
pre=[None for _ in range(n)]
next=[None for _ in range(n)]
for _ in range(q):
    c,p=map(int,input().split())
    c-=1
    p-=1
    if base[c]==c:
        base[c]=None
    pre[p]=c
    if next[c] is not None:
        pre[next[c]]=None
    next[c]=p
    # print(base)
    # print(pre)
    # print(next)
    # print('---------')

for i in range(n):
    if base[i]==None:
        print(0,end=' ')
    else:
        start=i
        count=1
        while pre[start] is not None:
            start=pre[start]
            count+=1
        print(count,end=' ')
