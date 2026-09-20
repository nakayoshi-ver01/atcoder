
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def rec(x,y):
    if x==y:
        return 0
    elif x<y:
        return rec(x,y//k)+1
    else:
        return rec(x//k,y)+1


for _ in range(t):
    x,y,k=map(int,input().split())
    print(rec(x,y))