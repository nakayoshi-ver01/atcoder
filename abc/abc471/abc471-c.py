from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()


# s=list(input())
# grid=[list(input()) for _ in range(h)]


ans=0
now=0

neg=deque()
pos=deque()
for i in a:
    if i>0:
        pos.append(i)
    else:
        neg.appendleft(i)

while pos and neg:
    p_side=pos.popleft()
    n_side=neg.popleft()

    if abs(now-n_side)<=abs(now-p_side):
        ans+=abs(now-n_side)
        now=n_side
        pos.appendleft(p_side)
    else:
        ans+=abs(now-p_side)
        now=p_side
        neg.appendleft(n_side)
while pos:
    p_side=pos.popleft()
    ans+=abs(now-p_side)
    now=p_side
while neg:
    n_side=neg.popleft()
    ans+=abs(now-n_side)
    now=n_side

print(ans)