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
mod=998244353

acc=[0]
for i in range(n):
    acc.append((acc[-1]+a[i])%mod)

def modeq(b,a,p):#一次合同式(分子,b:分母,a)
    z=b*pow(a,p-2,p)
    z%=p
    return z

log=[0]
for i in range(n//2+1):
    log.append(log[-1]+acc[n-i]-acc[i])

ans=0
for i in range(1,n+1):
    ans+=log[min(i,n-i+1)]*modeq(1,i,mod)
    ans%=mod
print(ans)