from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

nums=defaultdict(int)
for i in range(n):
    nums[a[i]]+=1



key=list(nums.keys())
key.sort()

count=0
ans=0
for i in range(101):
    if n-count>=i:
        ans=i
    count+=nums[i]
print(ans)