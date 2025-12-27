from collections import defaultdict,deque
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
for i in range(h):
    if 'S' in grid[i]:
       start=(i,grid[i].index('S'))
dans=100000000000
vans=100000000000

dque=deque()
vque=deque()
dque.append((0,start))
vque.append((0,start))
while dque:
    now=dque.popleft()
    if grid[now[1][0]][now[1][1]]=='G':
        dans=now[0]
        break
    
    if now[0]%2==0:
        if now[1][0]>0 and grid[now[1][0]-1][now[1][1]] in {'.','G'}:
            dque.append((now[0]+1,(now[1][0]-1,now[1][1])))
            if grid[now[1][0]-1][now[1][1]]=='.':
                grid[now[1][0]-1][now[1][1]]='o'
        if now[1][0]<h-1 and grid[now[1][0]+1][now[1][1]] in {'.','G'}:
            dque.append((now[0]+1,(now[1][0]+1,now[1][1])))
            if grid[now[1][0]+1][now[1][1]]=='.':
                grid[now[1][0]+1][now[1][1]]='o'
    else:
        if now[1][1]>0 and grid[now[1][0]][now[1][1]-1] in {'.','G'}:
            dque.append((now[0]+1,(now[1][0],now[1][1]-1)))
            if grid[now[1][0]][now[1][1]-1]=='.':
                grid[now[1][0]][now[1][1]-1]='o'
        if now[1][1]<w-1 and grid[now[1][0]][now[1][1]+1] in {'.','G'}:
            dque.append((now[0]+1,(now[1][0],now[1][1]+1)))
            if grid[now[1][0]][now[1][1]+1]=='.':
                grid[now[1][0]][now[1][1]+1]='o'
    # print(dque)
while vque:
    now=vque.popleft()
    if grid[now[1][0]][now[1][1]]=='G':
        vans=now[0]
        break
    if now[0]%2==1:
        if now[1][0]>0 and grid[now[1][0]-1][now[1][1]] in {'o','.','G'}:
            vque.append((now[0]+1,(now[1][0]-1,now[1][1])))
            if grid[now[1][0]-1][now[1][1]] in {'.','o'}:
                grid[now[1][0]-1][now[1][1]]='x'
        if now[1][0]<h-1 and grid[now[1][0]+1][now[1][1]] in {'o','.','G'}:
            vque.append((now[0]+1,(now[1][0]+1,now[1][1])))
            if grid[now[1][0]+1][now[1][1]] in {'.','o'}:
                grid[now[1][0]+1][now[1][1]]='x'
    else:
        if now[1][1]>0 and grid[now[1][0]][now[1][1]-1] in {'o','.','G'}:
            vque.append((now[0]+1,(now[1][0],now[1][1]-1)))
            if grid[now[1][0]][now[1][1]-1] in {'.','o'}:
                grid[now[1][0]][now[1][1]-1]='x'
        if now[1][1]<w-1 and grid[now[1][0]][now[1][1]+1] in {'o','.','G'}:
            vque.append((now[0]+1,(now[1][0],now[1][1]+1)))
            if grid[now[1][0]][now[1][1]+1] in {'.','o'}:
                grid[now[1][0]][now[1][1]+1]='x'

if min(dans,vans)!=100000000000:
    print(min(dans,vans))
else:
    print(-1)