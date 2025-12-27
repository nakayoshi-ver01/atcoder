# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
# import math
# import bisect
# import heapq
from functools import lru_cache
# n=int(input())
sys.setrecursionlimit(10**8)
h,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
grid=[list(map(int,input().split())) for _ in range(h)]

@lru_cache(maxsize=10000000)
def dfs(cover,score):
    global grid
    global h
    global w
    max_point=score
    for i in range(h):
        for j in range(w-1):
            if cover[i][j] and cover[i][j+1]:
                test=[[cover[l][k] for k in range(w)]for l in range(h)]
                test[i][j]=False
                test[i][j+1]=False
                for k in range(h):
                    test[k]=tuple(test[k])
                test=tuple(test)
                next_score=score^grid[i][j]^grid[i][j+1]
                ans=dfs(test,next_score)
                max_point=max(ans,max_point)
    
    for i in range(h-1):
        for j in range(w):
            if cover[i][j] and cover[i+1][j]:
                test=[[cover[l][k] for k in range(w)]for l in range(h)]
                test[i][j]=False
                test[i+1][j]=False
                for k in range(h):
                    test[k]=tuple(test[k])
                test=tuple(test)
                next_score=score^grid[i][j]^grid[i+1][j]
                ans=dfs(test,next_score)
                max_point=max(ans,next_score,max_point)
    return max_point

total=0
for i in range(h):
    for j in range(w):
        total^=grid[i][j]
ans=dfs(tuple(tuple(True for _ in range(w)) for _ in range(h)),total)
print(ans)