from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
from functools import lru_cache

import itertools
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]



@lru_cache(maxsize=10**6)
def rec(n:int,ali:list):
    global a
    if n==0:
        return sum(a)
    elif n==1:
        for i in a:
            d=[i]*(5-len(ali))
            throw=list(d)+ali
            throw.sort()
            rec(n-1,throw)
    elif n==2:
        for i in range(6-len(ali)):
            for j in a:
                d=[j]*i
                throw=list(d)+ali
                rec(n-1,throw)
    

ans=rec(2,[])