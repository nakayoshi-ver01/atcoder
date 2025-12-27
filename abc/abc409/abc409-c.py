from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,l=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


points=[0]
now=0
for i in range(n-1):
    points.append((now+a[i])%l)
    now+=a[i]


counter=defaultdict(set)
for i in range(n):
    counter[points[i]].add(i)
# print(counter)

ans=0
if l%3==0:
    for i in range(l//3):
        ans+=len(counter[i])*len(counter[i+l//3])*len(counter[i+2*(l//3)])

print(ans)