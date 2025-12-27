# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
t,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

fac_lis=[{}]
for i in range(1,5001):
    k=i
    tmp={}
    for j in fac_lis[-1]:
        tmp[j]=fac_lis[-1][j]
    for j in fac_lis[-1]:
        while k%j==0:
            tmp[j]+=1
            k//=j
    if k!=1:
        tmp[k]=1
    fac_lis.append(tmp)


for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    total=sum(c)
    bunbo=fac_lis[total]
    for i in c:
        divisor=fac_lis[i]
        for j in divisor:
            bunbo[j]-=divisor[j]
    ans=1
    for i in bunbo:
        for _ in range(bunbo[i]):
            ans*=i
        ans%=m
    print(ans)