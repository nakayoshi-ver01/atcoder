# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[input() for _ in range(n)]
flg=False
for i in range(n):
    for j in range(n):
        if i!=j:
            x=grid[i]+grid[j]
            rev_x=x[::-1]
            if x==rev_x:
                print('Yes')
                flg=True
                break
    if flg:
        break
else:
    print('No')