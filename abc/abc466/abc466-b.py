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

cl=[-1 for _ in range(m)]

for i in range(n):
    a,b=map(int,input().split())
    cl[a-1]=max(b,cl[a-1])

print(*cl)