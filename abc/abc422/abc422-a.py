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

if s[2]=='8':
    s[0]=str(int(s[0])+1)
    s[2]=str(1)
else:
    s[2]=str(int(s[2])+1)

print(''.join(s))