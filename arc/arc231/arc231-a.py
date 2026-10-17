# from collections import defaultdict,deque
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
# from functools import cmp_to_key, lru_cache

def dist_cost(monster,player):
    return (monster[0]-player[0])**2+(monster[1]-player[1])**2

for i in range(t):
    n=int(input())
    dp=[[[(0,0),0],[(0,0),0]]]
    for j in range(n):
        x,y,z=map(int,input().split())
        brade=min(dp[-1][0][1]+dist_cost(dp[-1][0][0],(x,y)),dp[-1][1][1]+dist_cost(dp[-1][1][0],(x,y)))
        magic=min(dp[-1][0][1],dp[-1][1][1])+z
        if dp[-1][0][1]<dp[-1][1][1]:
            dp.append([[(x,y),brade],[dp[-1][0][0],magic]])
        else:
            dp.append([[(x,y),brade],[dp[-1][1][0],magic]])
    print(min(dp[-1][0][1],dp[-1][1][1]))