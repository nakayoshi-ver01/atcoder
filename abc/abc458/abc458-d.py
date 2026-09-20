# from collections import defaultdict,deque
from sortedcontainers import SortedList
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
x=int(input())
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

p=SortedList()
p.add(x)
for i in range(q):
    a,b=map(int,input().split())
    p.add(a)
    p.add(b)
    print(p[i+1])