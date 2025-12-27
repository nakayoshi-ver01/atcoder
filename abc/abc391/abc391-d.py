# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n,w=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

stage=[[] for _ in range(w+1)]
blocks=[tuple(map(int,input().split())) for _ in range(n)]
max_array=[[0,0] for _ in range(n+1)]
count=0
for block in blocks:
    max_array[len(stage[block[0]])][0]+=1
    max_array[len(stage[block[0]])][1]=max(max_array[len(stage[block[0]])][1],block[1])
    stage[block[0]].append((block[1],count+1))
    count+=1
height=[0 for _ in range(n+1)]
for i in range(len(stage)):
    for j in range(len(stage[i])):
        height[stage[i][j][1]-1]=j+1


q=int(input())

for _ in range(q):
    query=tuple(map(int,input().split()))
    position=height[query[1]-1]
    if max_array[position-1][0]==w:
        if query[0]<max_array[position-1][1]:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')