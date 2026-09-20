from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

nums= defaultdict(int)
for i in range(n):
    nums[a[i]]+=1


p=[]
for key in nums.keys():
    p.append(nums[key]*key)

p.sort(reverse=True)

print(sum(p[k:]))