from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
import itertools
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
mtar=int(input())
taredge=defaultdict(set)
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(mtar):
    u,v=map(int,input().split())
    taredge[u-1].add(v-1)
    taredge[v-1].add(u-1)

mnow=int(input())
nowedge=defaultdict(set)
for _ in range(mnow):
    u,v=map(int,input().split())
    nowedge[u-1].add(v-1)
    nowedge[v-1].add(u-1)

cost=[list(map(int,input().split())) for _ in range(n-1)]



min_cost=10**10
for seq in list(itertools.permutations([i for i in range(n)])):
    same=defaultdict(set)
    for i in range(n):
        for j in taredge[i]:
            same[seq[i]].add(seq[j])
    totalcost=0
    for i in range(n):
        for j in range(i+1,n):
            if (j in same[i]) and (j not in nowedge[i]):
                totalcost+=cost[i][j-i-1]
            elif (j not in same[i]) and (j in nowedge[i]):
                totalcost+=cost[i][j-i-1]
    min_cost=min(totalcost,min_cost)

print(min_cost)