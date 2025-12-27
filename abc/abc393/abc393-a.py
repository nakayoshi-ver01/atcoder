# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(str,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if a[0]=='sick' and a[1]=='sick':
    print(1)
if a[0]=='sick' and a[1]=='fine':
    print(2)
if a[0]=='fine' and a[1]=='sick':
    print(3)
if a[0]=='fine' and a[1]=='fine':
    print(4)