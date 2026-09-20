# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


MOD=998244353

kaijo_log=[1]
for i in range(1,50+1):
    kaijo_log.append((kaijo_log[-1]*i)%MOD)

def combination(n,r):
    # 事前計算でn!,n-r!,r!を用意しておいて、nCrを計算する,(n,rともに一定の範囲内で何度も計算する場合に有効)
    return (kaijo_log[n]*pow(kaijo_log[r],MOD-2,MOD)*pow(kaijo_log[n-r],MOD-2,MOD))%MOD

if n==0:
    print('A')
else:    
    flg=False
    for i in range(1,50):
        for j in range(1,50-i):
            if i*j>=n:
                A=i
                C=j
                flg=True
                break
        if flg:
            break
    # print(A,C)
    arr=[]
    for i in range(A):
        arr.append('A')
        arr.append('R')
    for i in range(C-1):
        arr.append('C')
        arr.append('R')
    arr.append('C')
    # print(A*C-n)
    arr[2*(A-1)],arr[2*((A-1)+(A*C-n))]=arr[2*((A-1)+(A*C-n))],arr[2*(A-1)]
    print(''.join(arr))