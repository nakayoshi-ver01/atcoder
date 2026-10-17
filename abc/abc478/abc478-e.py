from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache



ans=[-1 for _ in range(n)]
edge=defaultdict(set)
rec_edge=defaultdict(int)

for _ in range(q):
    query=list(map(int,input().split()))
    edge[query[1]-1].add((query[0],query[2]-1))
    rec_edge[query[2]-1]+=1
print(rec_edge)
start=[]
for i in range(n):
    if rec_edge[i]==0:
        start.append(i)

print(start)
def rec():
    pass