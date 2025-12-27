# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
zekken=[-1 for _ in range(n+1)]
for i in range(n):
    zekken[q[i]]=i+1

for i in range(1,n+1):
    print(q[p[zekken[i]-1]-1],end=' ')