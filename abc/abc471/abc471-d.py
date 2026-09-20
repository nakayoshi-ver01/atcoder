# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
# n=int(input())
q,v=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


charger=[]

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        heapq.heappush(charger,query[1]+(v-query[2]))
    else:
        if charger:
            battery=heapq.heappop(charger)
            print(v-max(battery-query[1],0))
        else:
            print(-1)