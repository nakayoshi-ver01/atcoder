# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
count=0
for i in range(len(s)):
    if s[i]!=t[i]:
        count+=1
print(count)
# grid=[list(input()) for _ in range(h)]