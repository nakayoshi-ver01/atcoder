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
    s=list(input())
    s+=s
    for i in range(n):
        if s[i]=='0':
            s.append('1')
        else:
            s.append('0')
    r=0
    acc_irr=[0]
    for i in range(3*n):
        if s[i]=='0':
            acc_irr.append(max(0,acc_irr[-1]-1))
        else:
            acc_irr.append(acc_irr[-1]+1)

    print(acc_irr)