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
mapping=[]
for i in range(n):
    mapping.append((a[i],i+1))

mapping.sort()
for i in range(3):
    print(mapping[i][1],end=' ')
