# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
x,y,z=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

now=0

if now<x<y or y<x<now or x<now<y or y<now<x:
    print(abs(now-x))
elif now<z<y or y<z<now:
    print(abs(now-x))
elif z<now<y or y<now<z:
    print(abs(now-z)+abs(x-z))
else:
    print(-1)