# from collections import defaultdict,deque
# import sys
# import math
# import bisect
# import heapq
n=int(input())
import copy
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())


grid=[list(input()) for _ in range(n)]
mapping=copy.deepcopy(grid)
for i in range(n//2):
    
    if i%4==0:
        for j in range(i,n-i):
            mapping[i][n-1-j]=grid[j][i]
        for j in range(i,n-i):
            mapping[n-1-i][n-1-j]=grid[j][n-1-i]
        for k in range(i,n-i):
            mapping[k][n-1-i]=grid[i][k]
        for k in range(i,n-i):
            mapping[k][i]=grid[n-1-i][k]
    elif i%4==1:
        for j in range(i,n-i):
            mapping[j][i]=grid[n-1-j][n-1-i]
        for j in range(i,n-i):
            mapping[j][n-1-i]=grid[n-1-j][i]
        for k in range(i,n-i):
            mapping[i][k]=grid[n-1-i][n-1-k]
        for k in range(i,n-i):
            mapping[n-1-i][k]=grid[i][n-1-k]
    elif i%4==2:
        for j in range(i,n-i):
            mapping[n-1-i][j]=grid[j][i]
        for j in range(i,n-i):
            mapping[i][j]=grid[j][n-1-i]
        for k in range(i,n-i):
            mapping[n-1-k][i]=grid[i][k]
        for k in range(i,n-i):
            mapping[n-1-k][n-1-i]=grid[n-1-i][k]
    elif i%4==3:
        pass
 
for z in range(n):
    print(''.join(mapping[z]))