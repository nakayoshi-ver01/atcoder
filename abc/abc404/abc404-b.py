# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
import copy
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grida=[list(input()) for _ in range(n)]
gridb=[list(input()) for _ in range(n)]

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
    mapping=copy.deepcopy(grid)
    # mapping=[['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mapping[j][n-1-i]=grid[i][j]
    return mapping

ans=10**5

temp=0
for i in range(n):
    for j in range(n):
        if grida[i][j]!=gridb[i][j]:
            temp+=1
ans=min(ans,temp)

one=rotate(n,grida)
temp=0
for i in range(n):
    for j in range(n):
        if one[i][j]!=gridb[i][j]:
            temp+=1
ans=min(ans,temp+1)

two=rotate(n,one)

temp=0
for i in range(n):
    for j in range(n):
        if two[i][j]!=gridb[i][j]:
            temp+=1
ans=min(ans,temp+2)

three=rotate(n,two)

temp=0
for i in range(n):
    for j in range(n):
        if three[i][j]!=gridb[i][j]:
            temp+=1

ans=min(ans,temp+3)

print(ans)