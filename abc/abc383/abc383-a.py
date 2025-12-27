# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
now=0
ans=0
for i in range(n):
    t,v=map(int,input().split())
    diff=(t-now)
    ans=max(0,ans-diff)
    ans+=v
    now=t
print(ans)