from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

testimonies=[[] for _ in range(n)]
for i in range(n):
    a=int(input())
    for j in range(a):
        testimony=tuple(map(int,input().split()))
        testimonies[i].append(testimony)

max_honest=0
for i in range(1,2**n):
    k=i
    honest=set()
    for j in range(1,n+1):
        if k%2==1:
            honest.add(j)
        k//=2
        if k==0:
            break
    
    ok=set()
    for j in honest:
        ok.add(j)
    ng=set()
    flg=True
    while flg:
        flg=False
        cand=set()
        for j in ok:
            for k in testimonies[j-1]:
                if k[0] not in ok:
                    if k[1]==1:
                        cand.add(k[0])
                        flg=True
                if k[0] not in ng:    
                    if k[1]==0:
                        ng.add(k[0])
        ok|=cand
    
    if ok&ng:
        pass
    else:
        if honest&ng:
            pass
        else:
            max_honest=max(max_honest,len(honest))

print(max_honest)