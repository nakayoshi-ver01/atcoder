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
a.sort()
# s=list(input())
# grid=[list(input()) for _ in range(h)]

print(sum(a[:n-k]) if n-k>0 else 0)