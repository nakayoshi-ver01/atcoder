# from collections import defaultdict,deque
# from sortedcontainers import SortedList,SortedSet

import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
sys.setrecursionlimit(10**9)
log=list()
def dfs(k,m,lis):
    global log
    if len(lis)==k:
        log.append(lis)
        return 0
    else:
        for i in range(lis[-1]+10,m-(k-len(lis)-1)*10+1):
            dfs(k,m,lis+[i])

for i in range(1,m-(n-1)*10+1):
    dfs(n,m,[i])
print(len(log))
for i in log:
    print(*i)