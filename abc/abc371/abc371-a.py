# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
s=list(map(str,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if s[0]==s[2]:
    print('B')
if s[1]!=s[2] and s[0]!=s[2]:
    print('C')
if s[0]!=s[2] and s[1]==s[2]:
    print('A')
