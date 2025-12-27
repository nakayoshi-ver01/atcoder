# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
x,y=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

total=36

fail=0
for i in range(1,7):
    for j in range(1,7):
        if i+j<x and abs(i-j)<y:
            fail+=1

print(1-fail/total)