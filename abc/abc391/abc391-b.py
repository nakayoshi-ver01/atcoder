# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid1=[list(input()) for _ in range(n)]
grid2=[list(input()) for _ in range(m)]


for i in range(n-m+1):
    for j in range(n-m+1):
        flg=0
        for k in range(m):
            for l in range(m):
                if grid1[i+k][j+l]!=grid2[k][l]:
                    flg=1
                    break
            if flg==1:
                break
        else:
            flg=2
            print(i+1,j+1)
            break
    if flg==2:
        break
