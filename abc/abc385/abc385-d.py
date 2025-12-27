from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
# n=int(input())
n,m,sx,sy=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

housesx=defaultdict(list)
housesy=defaultdict(list)
for _ in range(n):
    a,b=map(int,input().split())
    housesx[a].append(b)
    housesy[b].append(a)
now=[sx,sy]
ans=0
for _ in range(m):
    d,l=map(str,input().split())
    l=int(l)
    if d=='U':
        p=bisect.bisect_left(housesx[now[0]],now[1])
        b=bisect.bisect_right(housesx[now[0]],now[1]+l)
        for i in reversed(range(p,b)):
            if housesy[housesx[now[0]][i]] and (now[0] in housesy[housesx[now[0]][i]]):
                housesy[housesx[now[0]][i]].remove(now[0])
            housesx[now[0]].remove(housesx[now[0]][i])
            ans+=1
        now[1]+=l
    if d=='D':
        p=bisect.bisect_left(housesx[now[0]],now[1])
        b=bisect.bisect_right(housesx[now[0]],now[1]-l)
        for i in reversed(range(b,p)):
            if housesy[housesx[now[0]][i]] and (now[0] in housesy[housesx[now[0]][i]]):
                housesy[housesx[now[0]][i]].remove(now[0])
            housesx[now[0]].remove(housesx[now[0]][i])
            ans+=1
        now[1]-=l
    if d=='R':
        p=bisect.bisect_left(housesy[now[1]],now[0])
        b=bisect.bisect_right(housesy[now[1]],now[0]+l)
        for i in reversed(range(p,b)):
            if housesx[housesy[now[1]][i]] and (now[1] in housesx[housesy[now[1]][i]]):
                housesx[housesy[now[1]][i]].remove(now[1])
            housesy[now[1]].remove(housesy[now[1]][i])
            ans+=1
        now[0]+=l
    if d=='L':
        p=bisect.bisect_left(housesy[now[1]],now[0])
        b=bisect.bisect_right(housesy[now[1]],now[0]-l)
        for i in reversed(range(b,p)):
            if housesx[housesy[now[1]][i]] and (now[1] in housesx[housesy[now[1]][i]]):
                housesx[housesy[now[1]][i]].remove(now[1])
            housesy[now[1]].remove(housesy[now[1]][i])
            ans+=1
        now[0]-=l
print(*now,ans)