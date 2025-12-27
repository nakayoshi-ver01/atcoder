from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
before=[True for _ in range(n)]
size=defaultdict(int)
for i in a:
    size[i]+=1
# s=list(input())
# grid=[list(input()) for _ in range(h)]

sizes=list(size.keys())
sizes.sort(reverse=True)
rui=[0]
for i in sizes:
    rui.append(size[i]+rui[-1])
rui.reverse()
sizes.reverse()
sizes.append(-1)
cur=0
ans=0
for i in sizes:
    while cur<len(rui)-1 and i*2>sizes[cur]:
        cur+=1
    ans+=size[i]*rui[cur]
print(ans)