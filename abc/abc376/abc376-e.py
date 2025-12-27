# from collections import defaultdict,deque
from sortedcontainers import SortedSet, SortedList, SortedDict
# import sys
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())

for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cal=list()
    
    for i,j in zip(a,b):
        cal.append((i,j))
    cal.sort()
    total=0
    front_k=0
    front_num=SortedList()
    for i in range(k):
        front_num.add(cal[i][1])
        front_k+=cal[i][1]
    ans=front_k*cal[i][0]
    for i in range(k,n):
        if front_num[k-1]>cal[i][1]:
            front_k-=front_num[k-1]-cal[i][1]
            front_num.add(cal[i][1])
        ans=min(front_k*cal[i][0],ans)
    print(ans)