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
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[]

    if n%2==1:
        b.append(a[-1])
        for i in range(n-1):
            b.append(a[i])
    else:
        b.append(a[-1])
        for i in range(n-1):
            b.append(a[i])
    ans=0
    for i in range(n-1):
        ans+=(b[i]+b[i+1])//2
    print(ans)