from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

import bisect
# n=int(input())
a = list(map(int,input().split()))
ans=0
length=[10**9 for _ in range(n+1)]
length[0]=0
dp=[0 for _ in range(n+1)]

querys=defaultdict(set)
for i in range(q):
    query=tuple(map(int,input().split()))
    querys[query[0]-1].add((i,query[1]))

ans_list=[0 for _ in range(q)]
for i in range(n):
    pos = bisect.bisect_left(length,a[i])
    dp[i] = pos

    length[dp[i]]=a[i]
    if querys[i]:
        for j in querys[i]:
            ans=bisect.bisect_right(length,j[1])
            ans_list[j[0]]=ans-1

for i in ans_list:
    print(i)



