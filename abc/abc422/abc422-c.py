# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    query=list(map(int,input().split()))
    ok=0
    ng=10**10
    while ok+1<ng:
        center=(ok+ng)//2
        tester=query[::]
        if tester[0]<center or tester[2]<center:
            ng=center
        else:
            tester[0]-=center
            tester[2]-=center
            if sum(tester)>=center:
                ok=center
            else:
                ng=center
    print(ok)