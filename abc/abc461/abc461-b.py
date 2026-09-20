# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for i in range(n):
    a[i]-=1
    b[i]-=1

for i in range(n):
    if b[a[i]]!=i:
        print('No')
        break
else:
    print('Yes')
