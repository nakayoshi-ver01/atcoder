# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ans=0
for i in range(1,n+1):
    x=i
    sum=0
    while x>0:
        sum+=x%10
        x//=10
    if sum==k:
        ans+=1

print(ans)