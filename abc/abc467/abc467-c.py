from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

a_zero=0
a_zero_test=[a[i] for i in range(n)]
if a_zero_test[0]!=0:
    a_zero+=1
    a_zero_test[0]=0
for i in range(n-1):
    if (a_zero_test[i]+a_zero_test[i+1])%m!=b[i]:
        a_zero_test[i+1]+=1
        a_zero+=1

a_one=0
a_one_test=[a[i] for i in range(n)]
if a_one_test[0]!=1:
    a_one+=1
    a_one_test[0]=1
for i in range(n-1):
    if (a_one_test[i]+a_one_test[i+1])%m!=b[i]:
        a_one_test[i+1]+=1
        a_one+=1
    # print(a_one,a_one_test)
print(min(a_zero,a_one))