# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]
min_step=[[10**6 for _ in range(w)] for _ in range(h)]
a,b,c,d=map(int,input().split())

a-=1
b-=1
c-=1
d-=1

min_step[a][b]=0
state=list()
heapq.heappush(state,(0,(a,b)))

while state:
    now=heapq.heappop(state)
    if now[1]==(c,d):
        print(now[0])
        break
    
    if now[1][0]>0:
        if grid[now[1][0]-1][now[1][1]]=='.' and min_step[now[1][0]-1][now[1][1]]>now[0]:
            heapq.heappush(state,(now[0],(now[1][0]-1,now[1][1])))
            min_step[now[1][0]-1][now[1][1]]=now[0]
        elif grid[now[1][0]-1][now[1][1]]=='#':
            if min_step[now[1][0]-1][now[1][1]]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0]-1,now[1][1])))
                min_step[now[1][0]-1][now[1][1]]=now[0]+1
            if now[1][0]>1 and min_step[now[1][0]-2][now[1][1]]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0]-2,now[1][1])))
                min_step[now[1][0]-2][now[1][1]]=now[0]+1
    if now[1][0]<h-1:
        if grid[now[1][0]+1][now[1][1]]=='.' and min_step[now[1][0]+1][now[1][1]]>now[0]:
            heapq.heappush(state,(now[0],(now[1][0]+1,now[1][1])))
            min_step[now[1][0]+1][now[1][1]]=now[0]
        elif grid[now[1][0]+1][now[1][1]]=='#':
            if min_step[now[1][0]+1][now[1][1]]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0]+1,now[1][1])))
                min_step[now[1][0]+1][now[1][1]]=now[0]+1
            if now[1][0]<h-2 and min_step[now[1][0]+2][now[1][1]]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0]+2,now[1][1])))
                min_step[now[1][0]+2][now[1][1]]=now[0]+1
    if now[1][1]>0:
        if grid[now[1][0]][now[1][1]-1]=='.' and min_step[now[1][0]][now[1][1]-1]>now[0]:
            heapq.heappush(state,(now[0],(now[1][0],now[1][1]-1)))
            min_step[now[1][0]][now[1][1]-1]=now[0]
        elif grid[now[1][0]][now[1][1]-1]=='#':
            if min_step[now[1][0]][now[1][1]-1]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0],now[1][1]-1)))
                min_step[now[1][0]][now[1][1]-1]=now[0]+1
            if now[1][1]>1 and min_step[now[1][0]][now[1][1]-2]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0],now[1][1]-2)))
                min_step[now[1][0]][now[1][1]-2]=now[0]+1
    if now[1][1]<w-1:
        if grid[now[1][0]][now[1][1]+1]=='.' and min_step[now[1][0]][now[1][1]+1]>now[0]:
            heapq.heappush(state,(now[0],(now[1][0],now[1][1]+1)))
            min_step[now[1][0]][now[1][1]+1]=now[0]
        elif grid[now[1][0]][now[1][1]+1]=='#':
            if min_step[now[1][0]][now[1][1]+1]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0],now[1][1]+1)))
                min_step[now[1][0]][now[1][1]+1]=now[0]+1
            if now[1][1]<w-2 and min_step[now[1][0]][now[1][1]+2]>now[0]+1:
                heapq.heappush(state,(now[0]+1,(now[1][0],now[1][1]+2)))
                min_step[now[1][0]][now[1][1]+2]=now[0]+1

