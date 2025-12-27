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
# s=list(input())
# grid=[list(input()) for _ in range(h)]

voter=[0 for _ in range(n)]
vote=[list(input()) for _ in range(n)]

for i in range(m):
    zero=0
    for j in range(n):
        if vote[j][i]=='0':
            zero+=1
    
    if zero in {n,0}:
        for j in range(n):
            voter[j]+=1
    elif zero<=n//2:
        for j in range(n):
            if vote[j][i]=='0':
                voter[j]+=1
    else:
        for j in range(n):
            if vote[j][i]=='1':
                voter[j]+=1
        
x=max(voter)

for i in range(n):
    if voter[i]==x:
        print(i+1, end=' ')
