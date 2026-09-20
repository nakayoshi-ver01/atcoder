# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
t,x=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

val=-1

for i in range(t+1):
    if val==-1:
        val=a[i]
        print(i,val)
    elif abs(val-a[i])>=x:
        val=a[i]
        print(i,val)

