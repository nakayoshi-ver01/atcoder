from collections import defaultdict,deque
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

char_num=defaultdict(int)

for i in s:
    char_num[i]+=1

z=list(char_num.values())
max_time=max(z)

for i in s:
    if char_num[i]!=max_time:
        print(i,end='')
print()