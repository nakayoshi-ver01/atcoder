from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
h,w,n=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

Garbage_col=defaultdict(set)
Garbage_row=defaultdict(set)

for i in range(n):
    x,y=map(int,input().split())
    Garbage_col[y].add(x)
    Garbage_row[x].add(y)

q=int(input())

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        print(len(Garbage_row[query[1]]))
        for i in Garbage_row[query[1]]:
            Garbage_col[i].remove(query[1])
        del Garbage_row[query[1]]
    elif query[0]==2:
        print(len(Garbage_col[query[1]]))
        for i in Garbage_col[query[1]]:
            Garbage_row[i].remove(query[1])
        del Garbage_col[query[1]]
    