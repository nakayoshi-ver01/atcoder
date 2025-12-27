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
# s=list(input())
# grid=[list(input()) for _ in range(h)]

cur=0
for i in range(n):
    if cur==0 or cur>i:
        cur=max(cur,i+a[i])
    else:
        print(i)
        break
else:
    print(n)