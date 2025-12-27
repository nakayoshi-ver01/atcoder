from collections import defaultdict,deque
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
rev_grid=[grid[i][::]for i in range(h)]

for i in range(h):
    for j in range(w):
        if grid[i][j]=='S':
            start=(i,j)
        elif grid[i][j]=='G':
            goal=(i,j)
        if rev_grid[i][j]=='x':
            rev_grid[i][j]='o'
        elif rev_grid[i][j]=='o':
            rev_grid[i][j]='x'

grids=[grid,rev_grid]

state=deque()
state.append((0,*start,0))

af=[[[True for _ in range(w)]for _ in range(h)]for _ in range(2)]
while state:
    now=state.popleft()
    if now[1]>0:
        if grids[now[0]][now[1]-1][now[2]]=='.' and af[now[0]][now[1]-1][now[2]]:
            state.append((now[0],now[1]-1,now[2],now[3]+1))
            af[now[0]][now[1]-1][now[2]]=False
        elif grids[now[0]][now[1]-1][now[2]]=='S' and af[now[0]][now[1]-1][now[2]]:
            state.append((now[0],now[1]-1,now[2],now[3]+1))
            af[now[0]][now[1]-1][now[2]]=False
        elif grids[now[0]][now[1]-1][now[2]]=='o' and af[now[0]][now[1]-1][now[2]]:
            state.append((now[0],now[1]-1,now[2],now[3]+1))
            af[now[0]][now[1]-1][now[2]]=False
        elif grids[now[0]][now[1]-1][now[2]]=='?' and af[(now[0]+1)%2][now[1]-1][now[2]]:
            state.append(((now[0]+1)%2,now[1]-1,now[2],now[3]+1))
            af[(now[0]+1)%2][now[1]-1][now[2]]=False
        elif grids[now[0]][now[1]-1][now[2]]=='G' and af[now[0]][now[1]-1][now[2]]:
            print(now[3]+1)
            break
    if now[1]<h-1:
        if grids[now[0]][now[1]+1][now[2]]=='.' and af[now[0]][now[1]+1][now[2]]:
            state.append((now[0],now[1]+1,now[2],now[3]+1))
            af[now[0]][now[1]+1][now[2]]=False
        elif grids[now[0]][now[1]+1][now[2]]=='S' and af[now[0]][now[1]+1][now[2]]:
            state.append((now[0],now[1]+1,now[2],now[3]+1))
            af[now[0]][now[1]+1][now[2]]=False
        elif grids[now[0]][now[1]+1][now[2]]=='o' and af[now[0]][now[1]+1][now[2]]:
            state.append((now[0],now[1]+1,now[2],now[3]+1))
            af[now[0]][now[1]+1][now[2]]=False
        elif grids[now[0]][now[1]+1][now[2]]=='?' and af[(now[0]+1)%2][now[1]+1][now[2]]:
            state.append(((now[0]+1)%2,now[1]+1,now[2],now[3]+1))
            af[(now[0]+1)%2][now[1]+1][now[2]]=False
        elif grids[now[0]][now[1]+1][now[2]]=='G' and af[now[0]][now[1]+1][now[2]]:
            print(now[3]+1)
            break
    if now[2]>0:
        if grids[now[0]][now[1]][now[2]-1]=='.' and af[now[0]][now[1]][now[2]-1]:
            state.append((now[0],now[1],now[2]-1,now[3]+1))
            af[now[0]][now[1]][now[2]-1]=False
        elif grids[now[0]][now[1]][now[2]-1]=='S' and af[now[0]][now[1]][now[2]-1]:
            state.append((now[0],now[1],now[2]-1,now[3]+1))
            af[now[0]][now[1]][now[2]-1]=False
        elif grids[now[0]][now[1]][now[2]-1]=='o' and af[now[0]][now[1]][now[2]-1]:
            state.append((now[0],now[1],now[2]-1,now[3]+1))
            af[now[0]][now[1]][now[2]-1]=False
        elif grids[now[0]][now[1]][now[2]-1]=='?' and af[(now[0]+1)%2][now[1]][now[2]-1]:
            state.append(((now[0]+1)%2,now[1],now[2]-1,now[3]+1))
            af[(now[0]+1)%2][now[1]][now[2]-1]=False
        elif grids[now[0]][now[1]][now[2]-1]=='G' and af[now[0]][now[1]][now[2]-1]:
            print(now[3]+1)
            break
    if now[2]<w-1:
        if grids[now[0]][now[1]][now[2]+1]=='.' and af[now[0]][now[1]][now[2]+1]:
            state.append((now[0],now[1],now[2]+1,now[3]+1))
            af[now[0]][now[1]][now[2]+1]=False
        elif grids[now[0]][now[1]][now[2]+1]=='S' and af[now[0]][now[1]][now[2]+1]:
            state.append((now[0],now[1],now[2]+1,now[3]+1))
            af[now[0]][now[1]][now[2]+1]=False
        elif grids[now[0]][now[1]][now[2]+1]=='o' and af[now[0]][now[1]][now[2]+1]:
            state.append((now[0],now[1],now[2]+1,now[3]+1))
            af[now[0]][now[1]][now[2]+1]=False
        elif grids[now[0]][now[1]][now[2]+1]=='?' and af[(now[0]+1)%2][now[1]][now[2]+1]:
            state.append(((now[0]+1)%2,now[1],now[2]+1,now[3]+1))
            af[(now[0]+1)%2][now[1]][now[2]+1]=False
        elif grids[now[0]][now[1]][now[2]+1]=='G' and af[now[0]][now[1]][now[2]+1]:
            print(now[3]+1)
            break
else:
    print(-1)