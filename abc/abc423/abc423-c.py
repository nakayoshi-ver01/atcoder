# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,r=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

most_left_unrock=-1
for i in range(r):
    if a[i]==0:
        most_left_unrock=i
        break

most_right_unrock=-1
for i in reversed(range(r,n)):
    if a[i]==0:
        most_right_unrock=i
        break

ans=0

if most_left_unrock!=-1:
    for i in range(most_left_unrock,r):
        if a[i]==1:
            ans+=1
    ans+=r-most_left_unrock
if most_right_unrock!=-1:
    for i in range(r,most_right_unrock):
        if a[i]==1:
            ans+=1
    ans+=most_right_unrock-(r-1)

print(ans)