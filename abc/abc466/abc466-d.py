from collections import defaultdict,deque
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

grid_h=defaultdict(set)
grid_w=defaultdict(set)


for _ in range(m):
    r,c=map(int,input().split())
    for i in grid_h[r-1]:
        grid_w[i].remove(r-1)
    for i in grid_w[c-1]:
        grid_h[i].remove(c-1)
    grid_h[r-1]={c-1}
    grid_w[c-1]={r-1}



ans=0
for i in grid_h:
    ans+=len(grid_h[i])

print(ans)