from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
p=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

flg=True
place=defaultdict(int)
inv_place=defaultdict(int)
for i in range(n):
    place[i+1]=p[i]
    inv_place[p[i]]=i+1

for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        if flg:
            a,b=place[query[1]],place[query[2]]
            inv_place[a],inv_place[b]=inv_place[b],inv_place[a]
            place[query[1]],place[query[2]]=place[query[2]],place[query[1]]
        else:
            a,b=inv_place[query[1]],inv_place[query[2]]
            place[a],place[b]=place[b],place[a]
            inv_place[query[1]],inv_place[query[2]]=inv_place[query[2]],inv_place[query[1]]
    else:
        flg=not flg

if flg:
    for i in range(1,n+1):
        print(place[i],end=' ')
else:
    for i in range(1,n+1):
        print(inv_place[i],end=' ')
