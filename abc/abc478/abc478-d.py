from collections import defaultdict,deque
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
# from functools import cmp_to_key, lru_cache


imos=[list() for _ in range(n+1)]
for _ in range(q):
    l,r,x=map(int,input().split())
    l-=1
    r-=1
    imos[l].append(x)
    imos[r+1].append(-x)

num_dict=defaultdict(int)
ans=set()
ans_list=list()
for i in range(n):
    for j in imos[i]:
        if j>0:
            num_dict[j]+=1
            ans.add(j)
        else:
            num_dict[-j]-=1
            if num_dict[-j]==0:
                ans.remove(-j)
    ans_list.append(len(ans))
print(*ans_list)