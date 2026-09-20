# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    s=list(input())
    k=int(input())

    count={i for i in range(len(s))}
    cur=0
    while cur<len(s)-2:
        if s[cur:cur+3]==['A','B','C']:
            count.discard(cur)
            count.discard(cur+1)
            count.discard(cur+2)
            cur+=3
        else:
            cur+=1
    if len(count)<3*k:
        print(-1)
    else:
        for i in range(len(s)):
            if i in count and (i+1 in count) and (i+2 in count):
                ans+=for