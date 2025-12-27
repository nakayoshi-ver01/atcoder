from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w,x,y=map(int,input().split())
x-=1
y-=1
# a=list(map(int,input().split()))
grid=[list(input()) for _ in range(h)]
s=list(input())

next=deque()
next.append((x,y))
now=[x,y]
ans=0
for i in s:
    if grid[now[0]][now[1]]=='@':
        ans+=1
        grid[now[0]][now[1]]='x'
    if i=='U' and now[0]>0 and grid[now[0]-1][now[1]]!='#':
        now[0]-=1
    if i=='D' and now[0]<h-1 and grid[now[0]+1][now[1]]!='#':
        now[0]+=1
    if i=='L' and now[1]>0 and grid[now[0]][now[1]-1]!='#':
        now[1]-=1
    if i=='R' and now[1]<w-1 and grid[now[0]][now[1]+1]!='#':
        now[1]+=1

if grid[now[0]][now[1]]=='@':
    ans+=1
    grid[now[0]][now[1]]='x'

now[0]+=1
now[1]+=1
print(*now,ans)