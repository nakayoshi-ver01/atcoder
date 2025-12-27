# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
import itertools 
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

b=[i for i in range(1,n+1)]

b_perm=list(itertools.permutations(b))

for i in b_perm:
    for j in range(n):
        if a[j]==i[j] or a[j]==-1:
            pass
        else:
            break
    else:
        print('Yes')
        print(*i)
        break
else:
    print('No')
