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
for i in range(n):
    acc.append(acc[-1]+a[i])

cur=0
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        cur+=query[1]
        cur%=n
    else:
        l=(query[1]-1+cur)%n+1
        r=(query[2]-1+cur)%n+1
        if l<=r:
            print(acc[r]-acc[l-1])
        else:
            print((acc[-1]-acc[l-1])+acc[r])
