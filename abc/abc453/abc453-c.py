# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
l=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=-1

for i in range(2**n):
    x=0.5
    pos=True
    k=i
    temp=0
    for j in range(n):
        if k%2==0:
            x+=l[j]
        else:
            x-=l[j]
        if pos and x<0:
            temp+=1
            pos=False
        elif not pos and x>0:
            temp+=1
            pos=True
        k//=2
    ans=max(ans,temp)
print(ans)