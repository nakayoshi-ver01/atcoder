from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

f=defaultdict(int)
for i in range(n):
    s=input()
    p=s.capitalize()
    f[p]+=1


z=0
for i in f:
    z=max(z,f[i])

print(z)