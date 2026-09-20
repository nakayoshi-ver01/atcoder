from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

rev=False


d=deque()
d.append(1)
for i in range(2,n+1):
    if s[i-1]=='o':
        rev=not rev
        if rev:
            d.appendleft(i)
        else:
            d.append(i)
    else:
        if not rev:
            d.appendleft(i)
        else:
            d.append(i)
if rev:
    while d:
        print(d.popleft(),end=' ')
else:
    while d:
        print(d.pop(),end=' ')
