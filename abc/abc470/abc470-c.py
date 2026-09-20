from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=[0 for _ in range(n)]
plus_set=set()
# s=list(input())
# grid=[list(input()) for _ in range(h)]


ans=0
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        query[1]-=1
        ans^=a[query[1]]
        ans^=a[query[1]]+1
        a[query[1]]+=1
        plus_set.add(query[1])
    else:
        rem_set=set()
        for j in plus_set:
            ans^=a[j]
            ans^=a[j]-1
            a[j]-=1
            if a[j]==0:
                rem_set.add(j)
        plus_set-=rem_set
    print(ans)