# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
d=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

rui=[0]
for i in range(n-1):
    rui.append(d[i]+rui[-1])


for i in range(n):
    for j in range(i+1,n):
        print(rui[j]-rui[i], end=' ')
    print()