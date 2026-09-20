# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

win_flg=False
for i in range(n):
    if a[i]>b[i]:
        win_flg=True
        break

w=[]
if win_flg:
    print('Yes')
    for i in range(n):
        if a[i]>b[i]:
            w.append(10**18)
        else:
            w.append(1)
    print(*w)
else:
    print('No')