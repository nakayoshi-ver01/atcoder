# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

acc_sum=[[0] for _ in range(10)]

for i in s:
    t=int(i)
    for j in range(10):
        if j==t:
            acc_sum[j].append(acc_sum[j][-1]+1)
        else:
            acc_sum[j].append(acc_sum[j][-1])

print(acc_sum)

ans=0
for i in range(len(s)):
    t=int(s[i])
    if t==0:
        continue
    else:
        t_num=acc_sum[t][i+1]
        tl_num=acc_sum[t-1][i+1]
        min_ts=min(t_num,tl_num)
        for j in range(1,min_ts+1):
            ans+=math.comb(t_num+tl_num,j)
            ans%=998244353
    print(ans)