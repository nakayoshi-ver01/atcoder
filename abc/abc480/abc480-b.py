# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

s=[]
vote=[0 for _ in range(n)]
for i in range(n):
    s.append(input())

for i in range(m):
    cand=-1
    t=input()
    for j in range(n):
        if len(s[j])==len(t):
            count=0
            for k in range(len(t)):
                if s[j][k]!=t[k]:
                    count+=1
            if count==0:
                vote[j]+=1
                break
            elif count==1 and cand==-1:
                cand=j
            elif count==1 and cand!=-1:
                cand=10**10
    else:
        if cand!=-1 and cand!=10**10:
            vote[cand]+=1

for i in vote:
    print(i)
