from collections import defaultdict,deque
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

house=defaultdict(bool)

for _ in range(m):
    a,b=map(str,input().split())
    if b=='M':
        if not house[int(a)]:
            print('Yes')
            house[int(a)]=True
        else:
            print('No')
    else:
        print('No')