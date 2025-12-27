# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0
for i in range(n):
    height=i+0.5
    width=pow(pow(n,2)-pow(height,2),0.5)
    box=int(width-0.5)
    if width>0.5:
        ans+=box*2+1
    if i>0:
        ans+=box*2+1
print(ans)