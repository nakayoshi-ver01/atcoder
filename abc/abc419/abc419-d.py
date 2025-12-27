# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())

swap=[0 for _ in range(n+1)]
# grid=[list(input()) for _ in range(h)]

for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    swap[a]+=1
    swap[b]-=1

acc=[swap[0]%2]

for i in range(1,n+1):
    acc.append((acc[-1]+swap[i])%2)


for i in range(n):
    if acc[i]==0:
        print(s[i],end='')
    else:
        print(t[i],end='')

