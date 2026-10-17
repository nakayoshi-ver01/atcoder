# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


acc_left=[10**10]
for i in range(n-1):
    acc_left.append(min(r[i],acc_left[-1]))

acc_right=[10**10]
for i in reversed(range(n-1)):
    acc_right.append(min(l[i],acc_right[-1]))

acc_right.reverse()
# print(acc_left)
# print(acc_right)

for _ in range(q):
    s,t=map(int,input().split())
    if s>t:
        if s==n:
            print(l[s-2])
        else:
            print(min(l[s-2],r[s-1]+acc_right[s-1]))
    else:
        if s==1:
            print(r[s-1])
        else:
            print(min(r[s-1],l[s-2]+acc_left[s-1]))
