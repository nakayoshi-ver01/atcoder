# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
n=int(input())
# grid=[list(input()) for _ in range(h)]


for i in range(n,len(s)-n):
    print(s[i],end='')