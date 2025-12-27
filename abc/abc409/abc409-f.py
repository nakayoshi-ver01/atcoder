from collections import defaultdict,deque
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

nearest=defaultdict(list)
pos=[]
for i in range(n):
    pos.append(list(map(int,input().split())))

for i in range(n):
    point=pos[i]
    for j in range(n):
        if i!=j:
            if not nearest[i]:
                nearest[i]=[j,abs(point[0]-pos[j][0])+abs(point[1]-pos[j][1])]
            else:
                if abs(point[0]-pos[j][0])+abs(point[1]-pos[j][1])<nearest[i][1]:
                    nearest[i]=[j,abs(point[0]-pos[j][0])+abs(point[1]-pos[j][1])]

for _ in range(q):
    querys=list(map(int,input().split()))
    if querys[0]==1:
        for i in range()