# from collections import defaultdict,deque
# import sys
# import math
import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
parts=list()
for _ in range(n):
    parts.append(tuple(map(int,input().split())))

parts.sort()
minr=[10**20]
for i in range(1,n+1): 
    minr.append(min(parts[-i][1],minr[-1]))
minr.reverse()

ans=0
for i in range(1,m+1):
    check_point = bisect.bisect_left(parts,(i,i))
    if check_point<=n-1:
        ans+=minr[check_point]-i
    else:
        ans+=m-i+1
print(ans)