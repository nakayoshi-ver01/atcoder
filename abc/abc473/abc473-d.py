# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache


def rec(i,k,arr):
    if i==n:
        if k%i==0:
            print(*(arr+[k//i]))
    else:
        roop=k//i
        if k%i==0:
            roop+=1
        for j in range(roop):
            rec(i+1,k-i*j,arr+[j])

rec(1,k,[])