# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# n=int(input())
n,m=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
# s=list(input())
# grid=[list(input()) for _ in range(h)]

rui=[0]
istart=list()
cur=0
for i in p:
    rui.append(rui[-1]+i)
rui.remove(0)
left=0
right=m
while left+1<right:
    center=(left+right)//2