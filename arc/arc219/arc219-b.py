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

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]!=1:
        print(0)
    else:
        ans=0
        if all(a[i]==i+1 for i in range(n)):
            ans+=1
        for i in range(n):
            if a[i]==i+1:
                ans+=n-i-1
            else:
                break
        print(ans%998244353)
