# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
b=[[] for _ in range(n)]

for i in range(n):
    k,*a=map(int,input().split())
    for j in a:
        b[j-1].append(i+1)

for i in range(n):
    print(len(b[i]),*b[i])