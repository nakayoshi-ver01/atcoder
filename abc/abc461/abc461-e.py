# from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

black_row=[-1 for _ in range(n)]
white_col=[-1 for _ in range(n)]
rows=SortedSet()
cols=SortedSet()
ans=0

for i in range(q):

    query=list(map(int,input().split()))
    query[1]-=1
    if query[0]==1:
        if black_row[query[1]]==-1:
            ans+=n
        else:
            rows.remove((black_row[query[1]],query[1]))
            ans+=len(cols)-cols.bisect_left((black_row[query[1]],-1))
        rows.add((i,query[1]))
        black_row[query[1]]=i
    else:
        if white_col[query[1]]!=-1:
            cols.remove((white_col[query[1]],query[1]))
            ans-=len(rows)-rows.bisect_left((white_col[query[1]],-1))
        else:
            ans-=len(rows)
        white_col[query[1]]=i
        cols.add((i,query[1]))
    print(ans)