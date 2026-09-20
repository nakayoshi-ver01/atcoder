from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

edge=defaultdict(set)

for _ in range(n-1):
    u,v=map(int,input().split())
    edge[u-1].add(v-1)
    edge[v-1].add(u-1)

bf=[True for _ in range(n)]
same=[False for _ in range(n)]
nums={a[0]}
def rec(place,flg):
    global nums
    for i in edge[place]:
        if bf[i]:
            bf[i]=False
            if (a[i] in nums) or flg:
                same[i]=True
                rec(i,True)
            else:
                nums.add(a[i])
                rec(i,False)
                nums.remove(a[i])

bf[0]=False
rec(0,False)

for i in range(n):
    if same[i]:
        print('Yes')
    else:
        print('No')