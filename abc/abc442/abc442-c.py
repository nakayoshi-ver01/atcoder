from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

peer = defaultdict(set)

for _ in range(m):
    a,b=map(int,input().split())
    peer[a].add(b)
    peer[b].add(a)

ans=[]
for i in range(1,n+1):
    k=n-len(peer[i])-1
    if k<3:
        ans.append(0)
    else:
        ans.append((k*(k-1)*(k-2))//6)

print(*ans)
