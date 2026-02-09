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
    n,w=map(int,input().split())
    box=[0 for _ in range(2*w)]
    c=list(map(int,input().split()))
    for i in range(n):
        box[i%(2*w)]+=c[i]
    cost=sum(box[:w])
    ans=cost
    for i in range(2*w):
        cost=cost-box[i%(2*w)]+box[(i+w)%(2*w)]
        ans=min(ans,cost)
    print(ans)