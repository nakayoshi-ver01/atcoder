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
# from functools import cmp_to_key, lru_cache

for _ in range(t):
    n,k=map(int,input().split())
    edge=defaultdict(dict)
    for i in range(n-1):
        l,r=map(int,input().split())
        edge[i]['l']=l-1
        edge[i]['r']=r-1
    num_place=[0 for _ in range(n)]
    num_place[0]=k
    for i in range(n-1):
        num_place[edge[i]['l']]+=num_place[i]//2
        num_place[edge[i]['r']]+=num_place[i]//2
        if num_place[i]%2==1:
            num_place[edge[i]['r']]+=1
    # print(num_place)
    print(sum(num_place[1:]))