# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(input()) for _ in range(h)]
ans=0
for i in range(h):
    for i_lim in range(i+1,h+1):
        for j in range(w):
            for j_lim in range(j+1,w+1):
                flg=True
                for k in range(i,i_lim):
                    for l in range(j,j_lim):
                        if grid[k][l]!=grid[i+i_lim-k-1][j+j_lim-l-1]:
                            flg=False
                            break
                    if not flg:
                        break
                else:
                    ans+=1
print(ans)