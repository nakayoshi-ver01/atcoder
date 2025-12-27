# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

lflg=False
uflg=False
double=True
af=set()
for i in s:
    if i.islower():
        lflg=True
    if i.isupper():
        uflg=True
    if i not in af:
        af.add(i)
    else:
        double=False

if lflg and uflg and double:
    print('Yes')
else:
    print('No')