# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
a,b,c=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

bunbo=1
mod=998244353

kaijo_log=[1]
for i in range(1,a+b+c+1):
    kaijo_log.append((kaijo_log[-1]*i)%mod)

ans=0

for i in range(1,min(b+1,a+1)):
    part_1=(kaijo_log[b+1]*pow(kaijo_log[i],mod-2,mod)*pow(kaijo_log[b+1-i],mod-2,mod))%mod
    part_2=(kaijo_log[a-1]*pow(kaijo_log[i-1],mod-2,mod)*pow(kaijo_log[a-1-(i-1)],mod-2,mod))%mod
    part_3=(kaijo_log[b+1-i-1+c]*pow(kaijo_log[b+1-i-1],mod-2,mod)*pow(kaijo_log[c],mod-2,mod))%mod
    temp=part_1
    temp*=part_2
    temp%=mod
    temp*=part_3
    temp%=mod
    ans+=temp
    ans%=mod
print(ans)