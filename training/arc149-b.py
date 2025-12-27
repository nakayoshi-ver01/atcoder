# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
import bisect





n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

sort_a=[0 for _ in range(n)]
for i in range(n):
    sort_a[b[i]-1]=a[i]
# 最長部分増加列
ans_a=0
length=[10**9 for _ in range(n+1)]
length[0]=0
dp=[0 for _ in range(n+1)]
for i in range(n):
    pos = bisect.bisect_left(length,sort_a[i])
    dp[i] = pos
    length[dp[i]]=sort_a[i]
    if dp[i]>ans_a:
        ans_a+=1

sort_b=[0 for _ in range(n)]
for i in range(n):
    sort_b[a[i]-1]=b[i]

# 最長部分増加列
ans_b=0
length=[10**9 for _ in range(n+1)]
length[0]=0
dp=[0 for _ in range(n+1)]
for i in range(n):
    pos = bisect.bisect_left(length,sort_b[i])
    dp[i] = pos
    length[dp[i]]=sort_b[i]
    if dp[i]>ans_b:
        ans_b+=1

print(max(ans_a,ans_b)+n)