# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
p=list()
for i in range(n):
    a=list(map(int,input().split()))
    p.append(a)

rui=[[0 for i in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        rui[i+1][j+1]=rui[i][j+1]+p[i][j]
print(rui)
# s=list(input())