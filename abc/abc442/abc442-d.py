# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

acc=[0]

for i in a:
    acc.append(acc[-1]+i)

for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        acc[query[1]]+=a[query[1]]-a[query[1]-1]
        a[query[1]-1],a[query[1]] = a[query[1]],a[query[1]-1]
    elif query[0]==2:
        l,r=query[1],query[2]
        print(acc[r]-acc[l-1])

