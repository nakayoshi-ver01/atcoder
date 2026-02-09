# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(q):
    x,y=map(int,input().split())
    border=bisect.bisect_left(a,x)
    ng=-1
    ok=n
    while ok-ng>1:
        center=(ok+ng)//2
        if (a[center]-x+1)-(center-border+1)>=y:
            ok=center
        else:
            ng=center
    print(x+(y-1)+(ok-border))