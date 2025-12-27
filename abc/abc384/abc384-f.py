from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

twodiv=defaultdict(list)
ansk=[0 for _ in range(28)]
for i in range(n):
    for j in range(28):
        mod=2**j
        if not twodiv[(j,(-a[i])%mod)]:
            twodiv[(j,(-a[i])%mod)].append(a[i])
        else:
            twodiv[(j,(-a[i])%mod)].append(a[i]+twodiv[(j,(-a[i])%mod)][-1])
        if len(twodiv[(j,a[i]%mod)])>0:
            ansk[j]+=len(twodiv[(j,a[i]%mod)])*a[i]+twodiv[(j,a[i]%mod)][-1]

ans=0
for i in range(27):
    ans+=(ansk[i]-ansk[i+1])//(2**i)
print(ans)