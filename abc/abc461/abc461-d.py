from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

n,m,k=map(int,input().split())
a=[list(map(int,input())) for _ in range(n)]

cumulative_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        cumulative_sum[i+1][j+1] = cumulative_sum[i+1][j]+a[i][j]


for i in range(n):
    for j in range(m):
        cumulative_sum[i+1][j+1] += cumulative_sum[i][j+1]


for i in range(n+1):
    print(cumulative_sum[i])

# k_value_num=defaultdict(int)
# row_one_num=[0 for _ in range(m)]
# col_one_num=[0 for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         if a[i][j]==1:
            