# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,s,l=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

ans=1
acc=[0]
for i in range(n-1):
    acc.append(acc[-1]+a[i])
# print(acc)
cur=s-1
for i in range(s):
    while cur<n-1 and (acc[s-1]-acc[i])*2+(acc[cur]-acc[s-1])<=l:
        # print((acc[s-1]-acc[i])*2,(acc[cur]-acc[s-1]),i,cur,'fff')
        cur+=1
        ans=max(ans,cur-i)
    if cur<n and (acc[s-1]-acc[i])*2+(acc[cur]-acc[s-1])<=l:
        cur+=1
        ans=max(ans,cur-i)
    # print(ans,s,cur,i)

cur=s-1
for i in reversed(range(s-1,n)):
    while cur>0 and (acc[i]-acc[s-1])*2+(acc[s-1]-acc[cur])<=l:
        # print((acc[i]-acc[s-1])*2,(acc[s-1]-acc[cur]),i,cur,'fff')
        cur-=1
        ans=max(ans,i-cur)
    if cur>-1 and (acc[i]-acc[s-1])*2+(acc[s-1]-acc[cur])<=l:
        cur-=1
        ans=max(ans,i-cur)
    # print(ans,s,cur,i)

print(ans)