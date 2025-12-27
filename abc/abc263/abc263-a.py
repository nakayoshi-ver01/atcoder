# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if (a.count(a[0])==3 and a.count(a[3])==2) or (a.count(a[0])==2 and a.count(a[3])==3):
    print('Yes')
else:
    print('No')