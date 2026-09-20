from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]

before = [[[False for _ in range(w)] for _ in range(h)] for _ in range(4)]

root=defaultdict(set)
dir_list=[(0,1),(1,0),(0,-1),(-1,0)]
dir_name=['R','D','L','U']

def back_track(now):
    if now[0] == -1:
        return None
    else:
        back_track(before[now[0]][now[1]][now[2]])
        print(dir_name[now[0]],end='')
        return None

for i in range(4):
    for j in range(h):
        for k in range(w):
            if grid[j][k] == '#':
                continue
            elif grid[j][k] == 'S':
                start = (j,k)
                for l in range(4):
                    if (0 <= j + dir_list[l][0] < h) and (0 <= k + dir_list[l][1] < w):
                        root[(-1,j,k)].add((l,j+dir_list[l][0],k+dir_list[l][1]))
            elif grid[j][k] == 'G':
                goal = (j,k)
            elif grid[j][k] == 'o':
                if (0 <= j + dir_list[i][0] < h) and (0 <= k + dir_list[i][1] < w):
                    root[(i,j,k)].add((i,j+dir_list[i][0],k+dir_list[i][1]))
            elif grid[j][k] == '.':
                for l in range(4):
                    if (0 <= j + dir_list[l][0] < h) and (0 <= k + dir_list[l][1] < w):
                        root[(i,j,k)].add((l,j+dir_list[l][0],k+dir_list[l][1]))
            elif grid[j][k] == 'x':
                for l in range(4):
                    if l != i:
                        if (0 <= j + dir_list[l][0] < h) and (0 <= k + dir_list[l][1] < w):
                            root[(i,j,k)].add((l,j+dir_list[l][0],k+dir_list[l][1]))

state=deque()
state.append((-1,start[0],start[1]))

before[0][start[0]][start[1]]=(-1,-1,-1)
before[1][start[0]][start[1]]=(-1,-1,-1)
before[2][start[0]][start[1]]=(-1,-1,-1)
before[3][start[0]][start[1]]=(-1,-1,-1)

while state:
    now=state.popleft()
    if (now[1],now[2]) == goal:
        print('Yes')
        back_track(now)
        break
    for next in root[now]:
        if not before[next[0]][next[1]][next[2]]:
            before[next[0]][next[1]][next[2]]=(now[0],now[1],now[2])
            state.append(next)
else:
    print('No')