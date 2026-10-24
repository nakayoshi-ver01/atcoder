# 事前準備したモジュールは以下のサイトに公開済み
# https://atcoder.jp/contests/abc100/submissions/80089964

# from collections import defaultdict,deque
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

if a[0]<k:
    below=True
    equal=False
    ans=0
elif a[0]==k:
    below=False
    equal=True
    ans=1
else:
    below=False
    equal=False
    ans=0

for i in range(1,n):
    if a[i]==k:
        ans+=1
        equal=True
        below=False
    elif a[i]>k:
        if equal:
            pass
        else:
            if below:
                ans+=1
            else:
                pass
        equal=False
        below=False
    else:
        if equal:
            pass
        else:
            if below:
                pass
            else:
                ans+=1
        equal=False
        below=True
print(ans)