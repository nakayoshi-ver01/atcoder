# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]
mod=998244353
now=''
combo=0
cur=0
ans=0
while cur<len(s):
    if now!=s[cur]:
        combo+=1
        now=s[cur]
    else:
        ans+=(combo*(combo+1))//2
        ans%=mod
        combo=1
    cur+=1
ans+=(combo*(combo+1))//2
ans%=mod

print(ans)