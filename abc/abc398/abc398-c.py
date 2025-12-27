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

numbers=defaultdict(set)
for i in range(n):
    numbers[a[i]].add(i+1)

keys=list(numbers.keys())
keys.sort(reverse=True)

for i in keys:
    if len(numbers[i])==1:
        print(numbers[i].pop())
        break
else:
    print(-1)
