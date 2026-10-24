# 事前準備したモジュールは以下のサイトに公開済み
# https://atcoder.jp/contests/abc100/submissions/80089964

from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

account=defaultdict(int)
names=set()

for _ in range(q):
    query=input()
    if query in names:
        print(account[query])
    else:
        account[query]=len(names)+1
        names.add(query)
        print(account[query])
