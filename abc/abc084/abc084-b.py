# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
a,b=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

for i in range(a+b+1):
    if i!=a:
        if not s[i].isdigit():
            print('No')
            break
    else:
        if s[i].isdigit():
            print('No')
            break
else:
    print('Yes')