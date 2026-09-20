from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

bomb_row=set()
bomb_col=set()

for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            bomb_col.add(i)
            bomb_row.add(j)


state=deque()

uncheck=[[True for _ in range(w)] for _ in range(h)]
ok=0
for i in range(h):
    for j in range(w):
        if (i not in bomb_col) and (j not in bomb_row):
            state.append((0,i,j))
            uncheck[i][j]=False
            ok+=1



dir=[[0,1],[1,0],[-1,0],[0,-1]]
while state:
    now=state.popleft()
    if now[0]<k:
        for i in dir:
            if (0<=now[1]+i[0]<h) and (0<=now[2]+i[1]<w) and grid[now[1]+i[0]][now[2]+i[1]]=='.' and uncheck[now[1]+i[0]][now[2]+i[1]]:
                uncheck[now[1]+i[0]][now[2]+i[1]]=False
                state.append((now[0]+1,now[1]+i[0],now[2]+i[1]))
                ok+=1

print(ok)