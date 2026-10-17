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

for _ in range(t):
    s=input()
    k=int(input())
    pal_num=[]
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            pal_num.append(i)

    ans=0
    r=0
    for i in range(len(pal_num)):
        while r<len(pal_num)-1 and pal_num[r+1]-pal_num[i]+3<=k:
            r+=1
        ans+=r-i+1
    print(ans)