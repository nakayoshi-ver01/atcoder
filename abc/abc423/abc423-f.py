# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
import itertools
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,y=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

pattern=list(itertools.combinations([i for i in range(n)],m))
print(len(pattern))

