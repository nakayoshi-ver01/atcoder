# from collections import defaultdict,deque
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

# ワーシャルフロイド法
n,m=map(int,input().split())
# 経路テーブル
path_length=[[10**20 for _ in range(n+1)] for _ in range(n+1)]
edges=list()
# 同じ場所はもちろん距離0
for i in range(n+1):
    path_length[i][i]=0
# 経路の記録
for i in range(m):
    a,b=map(int,input().split())
    edges.append((a,b))
    path_length[a][b]=1
    path_length[b][a]=1
# kを経由した際のi,j間の距離をそれぞれ計算しなおす
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            path_length[i][j]=min(path_length[i][j],path_length[i][k]+path_length[k][j])

print(path_length)

for i in edges:
    one_to_s=pa