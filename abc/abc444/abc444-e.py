# from collections import defaultdict,deque
from sortedcontainers import SortedList
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

box=SortedList()
ans=0
cur=0
for i in range(n):
    if not box:
        box.add(a[i])
        cur+=1
    while cur<n:
        smaller=box.bisect_right(a[cur])-1
        larger=box.bisect_left(a[cur])
        if abs(a[cur]-box[smaller])>=d:
            if larger<len(box) and abs(a[cur]-box[larger])>=d:
                box.add(a[cur])
                cur+=1
            elif larger==len(box):
                box.add(a[cur])
                cur+=1
            else:
                break
        else:
            break
    ans+=len(box)
    box.discard(a[i])
print(ans)