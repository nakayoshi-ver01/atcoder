# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=set(a)
b=list(b)
for i in range(len(b)):
    b[i]*=-1
heapq.heapify(b)
c=[0 for i in range(n)]
# s=list(input())
# grid=[list(input()) for _ in range(h)]

rank=1
for i in range(len(b)):
    count=0
    t=heapq.heappop(b)
    for j in range(n):
        if a[j]==-t:
            c[j]=rank
            count+=1
    rank+=count


for i in c:
    print(i)