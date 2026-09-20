from collections import deque
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

once_try=[['-' for j in range(w)] for i in range(h)]

check_dir=[(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]

state=deque()

ans_grid=[['-' for j in range(w)] for i in range(h)]
test_grid=[['-' for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            test_grid[i][j]='.'
            for di,dj in check_dir:
                if 0<=i+di<=h-1 and 0<=j+dj<=w-1 and grid[i+di][j+dj]!='#':
                    test_grid[i+di][j+dj]='#'

for i in range(h):
    for j in range(w):
        if test_grid[i][j]=='#':
            state.append((i,j,0))
            ans_grid[i][j]='.'

while state:
    i,j,dist=state.popleft()
    for di,dj in check_dir:
        if 0<=i+di<=h-1 and 0<=j+dj<=w-1 and ans_grid[i+di][j+dj]=='-':
            if dist%2==0:
                ans_grid[i+di][j+dj]='#'
            else:
                ans_grid[i+di][j+dj]='.'
            state.append((i+di,j+dj,dist+1))

if ans_grid[0][0]=='-':
    for k in range(h):
        print('.'*w)
else:
    for k in range(h):
        print(''.join(ans_grid[k]))
