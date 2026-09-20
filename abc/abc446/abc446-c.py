# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    total=0
    breaked=0
    used=0
    for i in range(n):
        total+=a[i]
        total-=b[i]
        used+=b[i]
        if i-d>=0:
            breaked+=a[i-d]
        if used<=breaked:
            total-=breaked-used
            used=breaked
    print(total)