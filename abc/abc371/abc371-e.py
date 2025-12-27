from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

num_pos=defaultdict(list)
for i in range(n):
    num_pos[a[i]].append(i)



ans=0
for i in num_pos:
    now=-1
    total=(n*(n+1))//2
    for j in num_pos[i]:
        dist=j-now-1
        total-=(dist*(dist+1))//2
        now=j
    dist=(n-1)-now
    total-=(dist*(dist+1))//2
    ans+=total
print(ans)