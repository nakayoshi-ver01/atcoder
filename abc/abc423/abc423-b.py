# from collections import defaultdict,deque
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

ans=set()
ans.add(0)
for i in range(n):
    if a[i]==0:
        ans.add(i+1)
    else:
        break

ans.add(n)
for i in reversed(range(n)):
    if a[i]==0:
        ans.add(i)
    else:
        break
# print(ans)
print(n+1-len(ans))