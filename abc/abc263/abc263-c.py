# from collections import defaultdict,deque
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

def monotonically_increasing(array):
    global n,m
    if len(array)==n:
        print(*array)
        return 0
    else:
        if array:
            for i in range(array[-1]+1,m+1):
                monotonically_increasing(array+[i])
        else:
            for i in range(1,m+1):
                monotonically_increasing(array+[i])

monotonically_increasing([])