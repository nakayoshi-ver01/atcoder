# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

lunch=[]
for i in range(n):
    bento=list(map(int,input().split()))
    lunch.append(bento)


ans=0
for i in range(1,2**n):
    k=i
    eat=set()
    cur=0
    while k>0:
        if k%2==1:
            eat.add(cur)
        k//=2
        cur+=1
    tmpa=0
    tmpb=0
    for j in eat:
        tmpa+=lunch[j][0]
        tmpb+=lunch[j][1]
    if tmpb<=w:
        ans=max(ans,tmpa)
print(ans)