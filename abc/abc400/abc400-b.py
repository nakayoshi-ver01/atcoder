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
# grid=[list(input()) for _ in range(h)]

ans=0
for i in range(m+1):
    if n**i>10**9:
        print('inf')
        break
    else:
        ans+=n**i
    if ans>10**9:
        print('inf')
        break
else:
    print(ans)