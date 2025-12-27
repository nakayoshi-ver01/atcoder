# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


array=[i+1 for i in range(n)]
rotate=0
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        array[(query[1]-1+rotate)%n]=query[2]
    elif query[0]==2:
        print(array[(query[1]-1+rotate)%n])
    else:
        rotate+=query[1]
