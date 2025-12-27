from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edge=defaultdict(set)
place=[]
for i in range(n):
    a=tuple(map(int,input().split()))
    place.append(a)

for i in range(n):
    for j in range(i+1,n):
        if (place[i][0]-place[j][0])**2+(place[i][1]-place[j][1])**2<=d**2:
            edge[i].add(j)
            edge[j].add(i)

af=[True for _ in range(n)]
state=deque()
state.append(0)
af[0]=False

while state:
    now=state.popleft()
    for i in edge[now]:
        if af[i]:
            af[i]=False
            state.append(i)

for i in range(n):
    print('Yes' if not af[i] else 'No')

