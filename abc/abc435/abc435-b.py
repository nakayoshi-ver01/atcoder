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
ans=0
for l in range(n):
    for r in range(l,n):
        k=sum(a[l:r+1])
        for i in range(l,r+1):
            if k%a[i]==0:
                break
        else:
            ans+=1

print(ans)