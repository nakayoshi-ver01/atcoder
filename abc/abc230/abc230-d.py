# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

walls=[]

for _ in range(n):
    wall=list(map(int,input().split()))
    walls.append(wall)

walls.sort(key=lambda x:x[1])

breaked=0
punch=1
pos=walls[breaked][1]
while breaked<n:
    if walls[breaked][0]<=pos+d-1:
        breaked+=1
    else:
        punch+=1
        pos=walls[breaked][1]
        breaked+=1
print(punch)
    