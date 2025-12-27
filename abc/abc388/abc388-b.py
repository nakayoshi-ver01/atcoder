# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
snakes=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,d+1):
    weight=list()
    for j in snakes:
        weight.append(j[0]*(j[1]+i))
    print(max(weight))