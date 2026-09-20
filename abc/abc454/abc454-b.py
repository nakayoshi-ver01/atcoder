# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
f=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

color=[0 for _ in range(m)]

for i in range(n):
    color[f[i]-1]+=1

print('Yes' if max(color)==1 else 'No')
print('Yes' if min(color)>0 else 'No')
