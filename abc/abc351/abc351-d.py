# from collections import defaultdict,deque
# import sys
# sys.setrecursionlimit(1000010)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
a=[list(input()) for _ in range(n)]
b=[list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j]!=b[i][j]:
            print(i+1,j+1)
            