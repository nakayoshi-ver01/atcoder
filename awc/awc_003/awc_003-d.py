# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

r=k-1

ans=0
total=sum(a[:r+1])

for i in range(n-k+1):
    while (r-i+1<k or total<m) and r<n-1:
        r+=1
        total+=a[r]
    
    if r-i+1>=k and total>=m:
        ans+=n-r
    total-=a[i]
print(ans)