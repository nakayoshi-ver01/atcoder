# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

depert=[0 for _ in range(m)]
next_depert=[0 for _ in range(m)]

for i in range(n):
    a,b=map(int,input().split())
    depert[a-1]+=1
    next_depert[b-1]+=1


for i in range(m):
    print(next_depert[i]-depert[i])

