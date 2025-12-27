# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
komoji=[chr(i) for i in range(97, 97+26)]
# grid=[list(input()) for _ in range(h)]
for i in komoji:
    if i not in s:
        print(i)
        break