# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

MOD=998244353

kaijo_log=[1]
for i in range(1,n+1):
    kaijo_log.append((kaijo_log[-1]*i)%MOD)

def combination(n,r):
    # 事前計算でn!,n-r!,r!を用意しておいて、nCrを計算する,(n,rともに一定の範囲内で何度も計算する場合に有効)
    return (kaijo_log[n]*pow(kaijo_log[r],MOD-2,MOD)*pow(kaijo_log[n-r],MOD-2,MOD))%MOD


if k==1:
    ans=0
    for i in a:
        ans+=i**2
        ans%=MOD
    print(ans)
else:
    comb_two_pow=combination(n-1,k-1)
    comb_double=combination(n-2,k-2)
    two_pow=0
    double=0
    total_sum=sum(a)
    for i in a:
        two_pow+=comb_two_pow*pow(i,2,MOD)
        two_pow%=MOD
    for i in a:
        double+=comb_double*i*(total_sum-i)
        double%=MOD

    
    ans=two_pow+double
    print(ans%MOD)