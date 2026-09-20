# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# from functools import lru_cache
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,l=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

# dp[life][c1][c2] : 未計算は None
dp=[[[None]*(n+1) for _ in range(n+1)] for _ in range(l+1)]

def rec(life,c1,c2):
    """
    life: ライフ
    c1: 片方だけ分かっている組数
    c2: 両方未判明の組数
    """
    if c2==0:
        return float(c1)
    if life==0:
        return 0.0

    memo=dp[life][c1][c2]
    if memo is not None:
        return memo

    tot=c1+c2+c2
    inv_tot=1.0/tot
    u2=c2+c2
    # (2*c2)/tot/(tot-1) を共通化
    base=u2*inv_tot/(tot-1)

    # unknown_pair
    ans=base*(1.0+rec(life,c1,c2-1))
    # known_pair
    if c1:
        ans+=c1*inv_tot*(1.0+rec(life,c1-1,c2))
    if life>1:
        # unknown_known
        ans+=base*c1*(1.0+rec(life-1,c1,c2-1))
        # not_pair
        if c2>1:
            ans+=base*(u2-2)*rec(life-1,c1+2,c2-2)

    dp[life][c1][c2]=ans
    return ans

ans=rec(l,0,n)*sum(a)/n
print(ans)
