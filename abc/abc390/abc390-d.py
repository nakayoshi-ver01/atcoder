# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import itertools
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
ans=set()
total=0
counter=0
def rec(k,now):
    global ans
    global a
    if k==n:
        z=0
        for i in now:
            if i:
                total=0
                for j in i:
                    total+=a[j]
                z^=total
        ans.add(z)
    else:
        for i in range(k+1):
            now[i].add(k)
            rec(k+1,now)
            now[i].remove(k)
            if not now[i]:
                break



rec(0,[set() for _ in range(n+1)])
print(len(ans))

