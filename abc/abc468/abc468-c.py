# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

import itertools 


base=[i for i in range(n)]
for i in range(n):
    a[i]-=1
    b[i]-=1

ans=0
for i in itertools.permutations(base):
    if a<list(i)<b:
        ans+=1

print(ans)