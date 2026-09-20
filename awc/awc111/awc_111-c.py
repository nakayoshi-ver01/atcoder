# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
h=list(map(int,input().split()))
t=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

imos=[0 for _ in range(n+1)]

for i in range(m):
    l,r,w=map(int,input().split())
    imos[l-1]+=w
    imos[r]-=w

rui=[0]
for i in range(n):
    rui.append(imos[i]+rui[-1])

ans=0
for i in range(n):
    if h[i]+rui[i+1]>=t[i]:
        ans+=1
# print(rui)
# print(imos)
print(ans)