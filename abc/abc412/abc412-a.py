# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
ans=0
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    if b>a:
        ans+=1
print(ans)
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]