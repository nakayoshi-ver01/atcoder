# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

a.sort()
b.sort()


a_cur=0
b_cur=0
while a_cur<n and b_cur<m:
    if b[b_cur] <= a[a_cur]*2:
        a_cur+=1
        b_cur+=1
    else:
        a_cur+=1

print(b_cur)