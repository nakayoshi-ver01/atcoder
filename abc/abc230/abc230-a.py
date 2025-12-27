# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=input()
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if int(n)<42:
    print(f'AGC{n.zfill(3)}')
else:
    print(f'AGC{str(int(n)+1).zfill(3)}')
