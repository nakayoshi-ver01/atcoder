# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
a=[]
for i in range(n):
    l,*c=map(int,input().split())
    a.append(c)

c=list(map(int,input().split()))

count=0
for i in range(n):
    if count+len(a[i])*c[i]<k:
        count+=len(a[i])*c[i]
    else:
        target=k-count-1
        print(a[i][target%len(a[i])])
        break