from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(map(int,input().split())) for _ in range(n-1)]
fullsize_edge=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n-i-1):
        fullsize_edge[i][j+i+1]=grid[i][j]
        fullsize_edge[j+i+1][i]=grid[i][j]

edge=defaultdict(set)
for i in range(1,n):
    root=list()
    for j in range(n):
        if i!=j and fullsize_edge[0][j]+fullsize_edge[j][i]==fullsize_edge[0][i]:
            root.append([fullsize_edge[j][i],j])
    root.sort()
    edge[i].add((root[0][1],root[0][0]))
    edge[root[0][1]].add((i,root[0][0]))


test=[[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    test[i][i]=0
def dfs(n,x,w):
    for i in edge[x]:
        if test[n][i[0]]==-1:
            test[n][i[0]]=w+i[1]
            test[i[0]][n]=w+i[1]
        if bf[i[0]]:
            bf[i[0]]=False
            dfs(n,i[0],w+i[1])
for i in range(n-1):
    bf=[True for _ in range(n)]
    bf[i]=False
    dfs(i,i,0)


for i in range(n):
    if fullsize_edge[i]!=test[i]:
        print('No')
        break
else:
    print('Yes')