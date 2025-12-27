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
# grid=[list(input()) for _ in range(h)]

kings=list()

for _ in range(n):
    king=list(map(int,input().split()))
    kings.append(king)


kings.sort()

xmax=kings[-1][0]
xmin=kings[0][0]

kings.sort(key=lambda x:x[1])

ymax=kings[-1][1]
ymin=kings[0][1]


xsummit=(xmax-xmin)//2+(xmax-xmin)%2
ysummit=(ymax-ymin)//2+(ymax-ymin)%2

print(max(xsummit,ysummit))