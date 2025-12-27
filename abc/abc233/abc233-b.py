# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
l,r=map(int,input().split())
# a=list(map(int,input().split()))
a=list(input())
# grid=[list(input()) for _ in range(h)]

t=a[:l-1]+list(reversed(a[l-1:r]))+a[r:]
print(''.join(t))