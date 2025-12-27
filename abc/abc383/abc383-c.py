from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]

search=deque()
for i in range(h):
    for j in range(w):
        if grid[i][j]=='H':
            search.append((i,j))
            grid[i][j]=0


while search:
    now=search.popleft()
    if grid[now[0]][now[1]]<d:
        if now[0]>0 and grid[now[0]-1][now[1]]=='.':
            grid[now[0]-1][now[1]]=grid[now[0]][now[1]]+1
            search.append((now[0]-1,now[1]))
        if now[1]>0 and grid[now[0]][now[1]-1]=='.':
            grid[now[0]][now[1]-1]=grid[now[0]][now[1]]+1
            search.append((now[0],now[1]-1))
        if now[0]<h-1 and grid[now[0]+1][now[1]]=='.':
            grid[now[0]+1][now[1]]=grid[now[0]][now[1]]+1
            search.append((now[0]+1,now[1]))
        if now[1]<w-1 and grid[now[0]][now[1]+1]=='.':
            grid[now[0]][now[1]+1]=grid[now[0]][now[1]]+1
            search.append((now[0],now[1]+1))
    
ans=0
for i in range(h):
    for j in range(w):
        if grid[i][j] not in {'.','#'}:
            ans+=1

print(ans)