# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
a=[]

for i in range(n):
    l,*c=map(int,input().split())
    a.append(c)

x,y=map(int,input().split())

print(a[x-1][y-1])