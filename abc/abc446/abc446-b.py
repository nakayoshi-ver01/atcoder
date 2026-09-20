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
cans=[True for _ in range(m)]
for _ in range(n):
    l=int(input())
    x=list(map(int,input().split()))
    for i in x:
        if cans[i-1]:
            cans[i-1]=False
            print(i)
            break
    else:
        print(0)
        