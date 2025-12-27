# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
x,y=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

def fib(n,x,y):
    if n<=1:
        return x
    elif n==2:
        return y
    else:
        b1=fib(n-1,x,y)
        b2=fib(n-2,x,y)
        x=b1+b2
        t=str(x)
        t=t[::-1]
        return int(t)


print(fib(10,x,y))