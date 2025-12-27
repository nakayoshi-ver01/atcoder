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

nums=defaultdict(int)

for i in range(n):
    nums[a[i]]+=1

set_a=set(a)
ans=0
for i in set_a:
    x=i
    for j in range(1,int(x**(1/2))+1):
        if x%j==0:
            y=j
            z=x//j
            if y!=z:
                ans+=nums[x]*nums[y]*nums[z]*2
            else:
                ans+=nums[x]*nums[y]*nums[z]
print(ans)