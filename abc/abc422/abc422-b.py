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
grid=[list(input()) for _ in range(h)]
flg=False
for i in range(h):
    for j in range(w):
        count=0
        if grid[i][j]=='#':
            if i>0 and grid[i-1][j]=='#':
                count+=1
            if i<h-1 and grid[i+1][j]=='#':
                count+=1
            if j>0 and grid[i][j-1]=='#':
                count+=1
            if j<w-1 and grid[i][j+1]=='#':
                count+=1
            if count not in {2,4}:
                flg=True
                print('No')
        if flg:
            break
    if flg:
        break
else:
    print('Yes')