# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import itertools 
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0
if k>=n-k:
    k=n-k
    x=itertools.combinations(a,k)
    allxor=0
    for i in a:
        allxor^=i
    for i in x:
        tmp=0
        for j in i:
            tmp^=j
        ans=max(ans,allxor^tmp)
    print(ans)
else:
    x=itertools.combinations(a,k)
    for i in x:
        tmp=0
        for j in i:
            tmp^=j
        ans=max(ans,tmp)
    print(ans)