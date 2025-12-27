# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
points={tuple(map(int,input().split())) for _ in range(n)}

ans=0

for i in points:
    for j in points:
        if i[0]==j[0] or i[1]==j[1]:
            continue
        else:
            if ((i[0],j[1]) in points) and ((j[0],i[1]) in points):
                ans+=1

print(ans//4)