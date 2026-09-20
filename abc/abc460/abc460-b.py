# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
for _ in range(t):
    a=list(map(int,input().split()))
    
    if ((a[3]-a[0])**2+(a[4]-a[1])**2)<=(a[2]+a[5])**2 and ((a[3]-a[0])**2+(a[4]-a[1])**2)>=(a[2]-a[5])**2:
        print('Yes')
    else:
        print('No')

