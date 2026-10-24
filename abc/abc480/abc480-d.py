# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

acc_a=[0]
for i in range(n):
    acc_a.append(acc_a[-1]+a[i])

acc_double=[0]
for i in range(1,len(acc_a)):
    acc_double.append(acc_double[-1]+acc_a[i])

acc_len_a=[(i*(i+1))//2 for i in range(n+1)]
print(acc_a)
print(acc_double)
print(acc_len_a)
for _ in range(q):
    l,r=map(int,input().split())
    l-=1
    st=bisect.bisect_left(acc_len_a,l)
    minus=acc_double[st]
    rem=(acc_a[st]-acc_a[st-(acc_len_a[st]-l)])
    minus-=rem
    gl=bisect.bisect_left(acc_len_a,r)
    plus=acc_double[gl-1]
    rem2=acc_a[gl-(acc_len_a[gl]-r)]
    plus+=rem2
    print(plus-minus)