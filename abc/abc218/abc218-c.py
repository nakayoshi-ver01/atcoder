# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
import copy

n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid_a_zero=[list(input()) for _ in range(n)]
grid_b_zero=[list(input()) for _ in range(n)]

def rotate(n,grid):
    """
    正方形のlistを回転させる:O(n^2)
    args:
        n:gridの大きさ
        grid:正方行列(list)
    return:
        mapping:90度回転させたgrid
    """
    # 作業用grid (空配列のほうが良いかも)
    mapping=[['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mapping[j][n-1-i]=grid[i][j]
    return mapping

grid_a=[grid_a_zero]
grid_b=[grid_b_zero]

for i in range(3):
    grid_a.append(rotate(n,grid_a[-1]))
    grid_b.append(rotate(n,grid_b[-1]))


grid_a_sharps=[]
grid_b_sharps=[]

for i in range(4):
    a_sharps=set()
    min_a_j=n
    min_a_k=n
    b_sharps=set()    
    min_b_j=n
    min_b_k=n
    for j in range(n):
        for k in range(n):
            if grid_a[i][j][k]=='#':
                min_a_j=min(min_a_j,j)
                min_a_k=min(min_a_k,k)
                a_sharps.add((j,k))
            if grid_b[i][j][k]=='#':
                min_b_j=min(min_b_j,j)
                min_b_k=min(min_b_k,k)
                b_sharps.add((j,k))
    parallel_a_sharps=set()
    parallel_b_sharps=set()

    for j in a_sharps:
        parallel_a_sharps.add((j[0]-min_a_j,j[1]-min_a_k))
    for j in b_sharps:
        parallel_b_sharps.add((j[0]-min_b_j,j[1]-min_b_k))
    
    grid_a_sharps.append(parallel_a_sharps)
    grid_b_sharps.append(parallel_b_sharps)

flg=False
for i in grid_a_sharps:
    for j in grid_b_sharps:
        for k in i:
            if k not in j:
                break
        else:
            for k in j:
                if k not in i:
                    break
            else:
                print('Yes')
                flg=True
        if flg:
            break
    if flg:
        break
else:
    print('No')