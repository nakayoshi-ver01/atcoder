# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,l,r=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
acc=[min(a[0],l)]

for i in range(1,n):
    acc.append(min(acc[-1]+a[i],l*(i+1)))

rev_acc=[min(a[-1],r)]
for i in range(1,n):
    rev_acc.append(min(rev_acc[-1]+a[n-1-i],r*(i+1)))

rev_acc.reverse()

most_min=10**15

# print(acc)
# print(rev_acc)
for i in range(n-1):
    most_min=min(most_min,acc[i]+rev_acc[i+1])

print(min(most_min,rev_acc[0],acc[-1]))