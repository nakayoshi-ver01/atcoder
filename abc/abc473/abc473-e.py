from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

acc=[0]

for i in range(n):
    acc.append((acc[-1]+a[i])%k)

same_mod=defaultdict(list)
for i in range(n+1):
    same_mod[acc[i]].append(i)

section=list()
for key in same_mod:
    for i in range(0,len(same_mod[key])-1):
        section.append((same_mod[key][i],same_mod[key][i+1]))

section.sort(key=lambda x:x[1])

# print(section)

ans=0
now=0
for i in section:
    if now<=i[0]:
        ans+=1
        now=i[1]

print(ans)