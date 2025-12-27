from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
edge=defaultdict(set)

for _ in range(n-1):
    a,b=map(int,input().split())
    edge[a].add(b)
    edge[b].add(a)

color=[-1 for _ in range(n+1)]
state=deque()
state.append((1,0))

while state:
    now=state.popleft()
    color[now[0]]=now[1]
    for i in edge[now[0]]:
        if color[i]==-1:
            state.append((i,1-now[1]))


cand=set()
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if (color[i]!=color[j]) and j not in edge[i]:
            cand.add((i,j))

if len(cand)%2==1:
    print('First')
    while cand:
        submit=cand.pop()
        print(*submit)
        rival=tuple(map(int,input().split()))
        if rival==(-1,-1):
            break
        else:
            cand.remove(rival)
else:
    print('Second')
    while cand:
        rival=tuple(map(int,input().split()))
        if rival==(-1,-1):
            break
        else:
            cand.remove(rival)
        submit=cand.pop()
        print(*submit)