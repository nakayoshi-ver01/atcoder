# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


ok=0
ng=2*(a[0]+k+1)

while ok+1<ng:
    center=(ok+ng)//2
    flg=True
    count=0
    for i in range(n):
        if center>=a[i]:
            count+=(center-a[i])//(i+1)+min(1,(center-a[i])%(i+1))
    if count<=k:
        ok=center
    else:
        ng=center
print(ok)