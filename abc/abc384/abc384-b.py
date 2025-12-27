# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,r=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(n):
    d,a=map(int,input().split())
    if d==1:
        if 1600<=r<=2799:
            r+=a
    if d==2:
        if 1200<=r<=2399:
            r+=a
print(r)