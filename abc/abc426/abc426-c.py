# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ver=[1 for i in range(n+1)]
right_chenge=0

oldest=1
for _ in range(q):
    x,y=map(int,input().split())
    if x<oldest:
        print(0)
    else:
        ans=0
        for i in range(oldest,x+1):
            ver[y]+=ver[i]
            ans+=ver[i]
            ver[i]=0
        oldest=x
        print(ans)