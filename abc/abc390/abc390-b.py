# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
for i in range(n-1):
    if a[0]*a[i+1]!=a[1]*a[i]:
        print('No')
        break
else:
    print('Yes')
