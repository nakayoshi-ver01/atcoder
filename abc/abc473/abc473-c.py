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
# from functools import cmp_to_key, lru_cache

classes=defaultdict(int)

for i in a:
    classes[i]+=1

biggest_member=0
for i in classes:
    biggest_member=max(classes[i],biggest_member)

ans=0
for i in range(1,k+1):
    if classes[i]+1>=biggest_member:
        ans+=1

print(ans)