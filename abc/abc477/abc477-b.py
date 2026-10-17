# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache
a_num=[]
for i in range(n):
    a_num.append((a[i],i+1))
a_num.sort()
ans=[]
for i in range(n):
    flg=True
    if i!=0:
        if a_num[i][0]-a_num[i-1][0]<d:
            flg=False
    if i!=n-1:
        if a_num[i+1][0]-a_num[i][0]<d:
            flg=False
    if flg:
        ans.append(a_num[i][1])

ans.sort()
print(len(ans))
print(*ans)