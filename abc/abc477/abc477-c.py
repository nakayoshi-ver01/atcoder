# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

T=len(t)
same=[]
for i in range(len(s)-T+1):
    if t==s[i:i+T]:
        same.append((i,i+T-1))

same_set=set(same)
for i in range(n):
    query=list(map(int,input().split()))
    query[0]-=1
    query[1]-=1
    if query[1]-query[0]<T-1:
        print('No')
    else:
        if tuple(query) in same_set:
            print('Yes')
        else:
            left=bisect.bisect_left(same,(query[0],query[0]+T-1))
            right=bisect.bisect_right(same,(query[1]-T+1,query[1]))
            if left==right:
                print('No')
            else:
                print('Yes')
        