# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=[[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if 0<i:
            ans[i][j]+=1
        if 0<j:
            ans[i][j]+=1
        if i<h-1:
            ans[i][j]+=1
        if j<w-1:
            ans[i][j]+=1

for i in range(h):
    for j in range(w):
        print(ans[i][j],end=' ')
    print()