from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

MOD = 998244353
edge=defaultdict(set)
for i in range(n-1):
    edge[p[i]-1].add(i+1)

kaijo_log=[1]
for i in range(1,10**6+1):
    kaijo_log.append((kaijo_log[-1]*i)%MOD)

def kaijomod(st,gl):
    ans=1
    for i in range(st):
        ans*=gl-i
        ans%=MOD
    return ans

def dfs(now):
    if not edge[now]:
        if d[now]>c[now]:
            return 0,0
        else: 
            return (kaijomod(d[now],c[now])*pow(kaijo_log[d[now]],MOD-2,MOD))%MOD, c[now]-d[now]

    else:
        pattern=1
        remain=c[now]
        for i in edge[now]:
            pattern_i, remain_i = dfs(i)
            pattern*=pattern_i
            pattern%=MOD
            remain+=remain_i
        if d[now]>remain or pattern==0:
            return 0,0
        else:
            return (pattern*kaijomod(d[now],remain)*pow(kaijo_log[d[now]],MOD-2,MOD))%MOD, remain-d[now]

ans, _ = dfs(0)
print(ans)