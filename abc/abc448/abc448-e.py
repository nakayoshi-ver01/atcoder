# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
k,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


def modeq(b,a,p):#一次合同式(分子,b:分母,a)
    z=b*pow(a,p-2,p)
    z%=p
    return z

MOD=10007
REV_NINE=modeq(1,9,MOD)
cl=[list(map(int,input().split())) for _ in range(k)]

total_dig=0
total_mod=0
for dig in reversed(cl):
    total_mod+=(pow(10,total_dig,MOD)*(pow(10,dig[1],MOD)-1)*REV_NINE*dig[0])%MOD
    total_mod%=MOD
    total_dig+=dig[1]

total_mod*=modeq(1,m,MOD)
total_mod%=MOD

print(total_mod)