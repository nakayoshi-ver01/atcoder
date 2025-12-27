# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
if a[0]==a[1]*a[2] or a[2]==a[1]*a[0] or a[1]==a[0]*a[2]:
    print('Yes')
else:
    print('No')