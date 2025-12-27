# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
person=['A','B','C','D','E']
rank=list()
for i in range(32):
    z=i
    name=''
    point=0
    cur=0
    while z>0:
        if z%2==1:
            name+=person[cur]
            point+=a[cur]
        z//=2
        cur+=1
    rank.append((point,name))


rank.sort(key=lambda x:(-1*x[0],x[1]))
for i in rank:
    print(i[1])