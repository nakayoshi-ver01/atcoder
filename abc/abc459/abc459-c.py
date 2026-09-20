# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
imos=[n for _ in range(q+1)]

base=0
pos=[0 for _ in range(n)]
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        pos[query[1]-1]+=1
        imos[pos[query[1]-1]-1]-=1
        if imos[base]==0:
            base+=1
    else:
        if base+query[1]-1<q+1:
            print(n-imos[base+query[1]-1])
        else:
            print(n-imos[q])