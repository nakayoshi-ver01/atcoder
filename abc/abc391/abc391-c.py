# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

Pigeon = [{i} for i in range(n+1)]
Pigeon_Hole = [i for i in range(n+1)]
ans=0
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        Pigeon_position=Pigeon_Hole[query[1]]
        if len(Pigeon[query[2]])==1:
            ans+=1
        Pigeon[query[2]].add(query[1])
        if len( Pigeon[Pigeon_position])==2:
            ans-=1
        Pigeon[Pigeon_position].remove(query[1])
        Pigeon_Hole[query[1]]=query[2]
    else:
        print(ans)