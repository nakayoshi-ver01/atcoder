from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

acc=[0]
for i in range(n):
    acc.append(acc[-1]+a[i])

count=defaultdict(int)
ans=0
for i in range(n+1):
    ans+=count[acc[i]-k]
    count[acc[i]]+=1

print(ans)