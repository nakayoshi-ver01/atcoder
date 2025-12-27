# from collections import defaultdict,deque
from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
n=int(input())
# n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
line=[-1 for _ in range(n+1)]
p=SortedList([i for i in range(n+1)])
for i in reversed(range(n)):
    place=p[a[i]]
    # diff=p.bisect_left(place)
    # print(diff)
    # place=p[diff]
    line[place]=i+1
    p.discard(place)
print(*line[1:])
