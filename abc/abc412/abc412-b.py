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
t=set(input())
# grid=[list(input()) for _ in range(h)]

for i in range(1,len(s)):
    if s[i].isupper():
        if s[i-1] not in t:
            print('No')
            break
else:
    print('Yes')