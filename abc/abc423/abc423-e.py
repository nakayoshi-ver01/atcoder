# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
b=[a[i]*(i+1) for i in range(n)]
c=[b[0]]
for i in range(n):
    c.append(c[-1]+b[i])
print(b)
print(c)
d=[a[i]*(n-i) for i in range(n)]
e=[d[0]]
for i in range(n):
    c.append(c[-1]+b[i])
print(d)
print(e)
# s=list(input())
# grid=[list(input()) for _ in range(h)]