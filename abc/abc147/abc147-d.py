# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
box=[0 for _ in range(60)]
for i in a:
    k=i
    for j in range(60):
        box[j]+=k%2
        k//=2

ans=0
for i in range(60):
    ans+=pow(2,i,10**9+7)*box[i]*(n-box[i])
    ans%=10**9+7
print(ans)