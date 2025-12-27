from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

groups=deque()
for _ in range(n):
    group=list(map(int,input().split()))
    groups.append(group)
capacity=k
eating=list()
time=0
while groups:
    next_group=groups.popleft()
    if next_group[2]<=capacity:
        capacity-=next_group[2]
        heapq.heappush(eating,[max(time,next_group[0])+next_group[1],next_group[2]])
        print(max(time,next_group[0]))
    else:
        while next_group[2]>capacity:
            eating_group=heapq.heappop(eating)
            time=eating_group[0]
            capacity+=eating_group[1]
        capacity-=next_group[2]
        heapq.heappush(eating,[max(time,next_group[0])+next_group[1],next_group[2]])
        print(max(time,next_group[0]))
        
        