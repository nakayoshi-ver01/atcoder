# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

for i in range(n):
    if s[i]=='G':
        for j in range(1,min(m+1,i+1)):
            if s[max(i-j,0)]=='.':
                s[max(i-j,0)]='x'
        for j in range(1,min(m+1,n-i+1)):
            if s[min(i+j,n-1)]=='.':
                s[min(i+j,n-1)]='x'
print(s.count('.'))