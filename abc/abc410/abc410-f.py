# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


# 二次元累積和
for _ in range(t):
    h,w=map(int,input().split())
    grid=[list(input()) for _ in range(h)]

    cumulative_sum_a = [[0 for _ in range(w+1)] for _ in range(h+1)]

    for i in range(h):
        for j in range(w):
            if grid[i][j]=='#':
                cumulative_sum_a[i+1][j+1] = cumulative_sum_a[i+1][j]+1
            else:
                cumulative_sum_a[i+1][j+1] = cumulative_sum_a[i+1][j]


    for i in range(h):
        for j in range(w):
            cumulative_sum_a[i+1][j+1] += cumulative_sum_a[i][j+1]


    for i in range(h+1):
        print(cumulative_sum_a[i])

    print('--------------------')
    cumulative_sum_b = [[0 for _ in range(w+1)] for _ in range(h+1)]

    for i in range(h):
        for j in range(w):
            if grid[i][j]=='.':
                cumulative_sum_b[i+1][j+1] = cumulative_sum_b[i+1][j]+1
            else:
                cumulative_sum_b[i+1][j+1] = cumulative_sum_b[i+1][j]


    for i in range(h):
        for j in range(w):
            cumulative_sum_b[i+1][j+1] += cumulative_sum_b[i][j+1]


    for i in range(h+1):
        print(cumulative_sum_b[i])
    
    ans=0
    for i in range(h):
        for j in range(w):
            total_a=cumulative_sum_a[i][j]