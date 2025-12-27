# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]

stoneleft=10000
stoneright=-1
stoneup=10000
stonedown=-1

for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            stoneleft=min(j,stoneleft)
            stoneright=max(j,stoneright)
            stoneup=min(i,stoneup)
            stonedown=max(i,stonedown)

flg=0
for i in range(stoneup,stonedown+1):
    for j in range(stoneleft,stoneright+1):
        if grid[i][j]=='.':
            flg=1
            print('No')
            break
    if flg:
        break
else:
    print('Yes')