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
products=[list(map(int,input().split())) for _ in range(n)]

products.sort(key=lambda x:x[1]-x[0])

# print(products)
ans=0
for i in range(n):
    if i<k:
        ans+=products[i][1]
    else:
        ans+=products[i][0]

print(ans)

