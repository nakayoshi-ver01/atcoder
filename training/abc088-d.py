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

wall=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            wall+=1


states=deque()
states.append((0,0))
grid[0][0]=1
while states:
    now=states.popleft()
    if now==(h-1,w-1):
        print(
            h*w-grid[h-1][w-1]-wall
        )
        break
    if now[0]>0 and grid[now[0]-1][now[1]]=='.':
        grid[now[0]-1][now[1]]=grid[now[0]][now[1]]+1
        states.append((now[0]-1,now[1]))
    if now[0]<h-1 and grid[now[0]+1][now[1]]=='.':
        grid[now[0]+1][now[1]]=grid[now[0]][now[1]]+1
        states.append((now[0]+1,now[1]))
    if now[1]>0 and grid[now[0]][now[1]-1]=='.':
        grid[now[0]][now[1]-1]=grid[now[0]][now[1]]+1
        states.append((now[0],now[1]-1))
    if now[1]<w-1 and grid[now[0]][now[1]+1]=='.':
        grid[now[0]][now[1]+1]=grid[now[0]][now[1]]+1
        states.append((now[0],now[1]+1))
else:
    print(-1)