# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
h,w,x=map(int,input().split())
p,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(map(int,input().split())) for _ in range(h)]

next=list()
t=grid[p-1][q-1]
grid[p-1][q-1]=-1
if p>1:
    heapq.heappush(next,(grid[p-2][q-1],(p-2,q-1)))
if q<w:
    heapq.heappush(next,(grid[p-1][q],(p-1,q)))
if p<h:
    heapq.heappush(next,(grid[p][q-1],(p,q-1)))
if q>1:
    heapq.heappush(next,(grid[p-1][q-2],(p-1,q-2)))
while next:
    now=heapq.heappop(next)
    if now[0]<t/x and grid[now[1][0]][now[1][1]]!=-1:
        t+=now[0]
        grid[now[1][0]][now[1][1]]=-1
        if now[1][0]>0 and grid[now[1][0]-1][now[1][1]]!=-1:
            heapq.heappush(next,(grid[now[1][0]-1][now[1][1]],(now[1][0]-1,now[1][1])))
        if now[1][0]<h-1 and grid[now[1][0]+1][now[1][1]]!=-1:
            heapq.heappush(next,(grid[now[1][0]+1][now[1][1]],(now[1][0]+1,now[1][1])))
        if now[1][1]<w-1 and grid[now[1][0]][now[1][1]+1]!=-1:
            heapq.heappush(next,(grid[now[1][0]][now[1][1]+1],(now[1][0],now[1][1]+1)))
        if now[1][1]>0 and grid[now[1][0]][now[1][1]-1]!=-1:
            heapq.heappush(next,(grid[now[1][0]][now[1][1]-1],(now[1][0],now[1][1]-1)))

print(t)