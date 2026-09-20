from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

nums={}
for i in range(n):
    if a[i]-1 in nums:
        nums[a[i]] = nums[a[i]-1] + 1
    else:
        nums[a[i]] = 1

print(max(nums.values()))