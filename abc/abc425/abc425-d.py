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

def checker(i,j):
    global grid
    global h
    global w
    count=0
    if i>0 and grid[i-1][j]=='#':
        count+=1
    if i<h-1 and grid[i+1][j]=='#':
        count+=1
    if j>0 and grid[i][j-1]=='#':
        count+=1
    if j<w-1 and grid[i][j+1]=='#':
        count+=1
    return count


cand=set()
for i in range(h):
    for j in range(w):
        if checker(i,j)==1 and grid[i][j]!='#':
            cand.add((i,j))

state=deque()
while cand:
    state.append(cand.pop())
turn=0
while state:
    turn+=1
    while state:
        now=state.popleft()
        grid[now[0]][now[1]]='#'
        if now[0]>0 and grid[now[0]-1][now[1]]=='.':
            cand.add((now[0]-1,now[1]))
        if now[0]<h-1 and grid[now[0]+1][now[1]]=='.':
            cand.add((now[0]+1,now[1]))
        if now[1]>0 and grid[now[0]][now[1]-1]=='.':
            cand.add((now[0],now[1]-1))
        if now[1]<w-1 and grid[now[0]][now[1]+1]=='.':
            cand.add((now[0],now[1]+1))

    
    while cand:
        i=cand.pop()
        if checker(i[0],i[1])==1:
            state.append(i)
        else:
            if grid[i[0]][i[1]]=='.':
                grid[i[0]][i[1]]='-'


ans=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=='#':
            ans+=1

print(ans)