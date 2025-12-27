# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
a,b,c,d,e,f,x=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

takahashi=(a*b)*(x//(a+c))+b*min(a,x%(a+c))
aoki=(d*e)*(x//(d+f))+e*min(d,x%(d+f))

if takahashi>aoki:
    print('Takahashi')
elif takahashi<aoki:
    print('Aoki')
else:
    print('Draw')

