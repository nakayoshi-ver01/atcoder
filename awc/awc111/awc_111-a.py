# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

fail=0
for i in range(n):
    s=list(map(int,input().split()))
    s.sort()
    if m>=3:
        score=sum(s[1:-1])//(m-2)
    else:
        score=sum(s)//m
    
    if score<k:
        fail+=1
print(fail)