# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(str,input().split())
ver=[ "Ocelot", "Serval", "Lynx" ]
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if ver.index(n)>=ver.index(m):
    print('Yes')
else:
    print('No')