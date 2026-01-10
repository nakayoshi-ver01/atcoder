# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
doubling=[[(i+1,a[i]-1) for i in range(n)]]
for k in range(29):
    tmp=[]
    for i in range(n):
        tmp.append(
            (
                doubling[-1][doubling[-1][i][1]][0]+doubling[-1][i][0],
                doubling[-1][doubling[-1][i][1]][1]
            )
        )
    doubling.append(tmp)

for _ in range(q):
    t,b=map(int,input().split())
    x=[]
    b-=1
    tmp=0
    while t>0:
        if t%2==1:
            x.append(tmp)
        t//=2
        tmp+=1
    x.reverse()
    ans=0
    for i in x:
        ans+=doubling[i][b][0]
        b=doubling[i][b][1]
    print(ans)