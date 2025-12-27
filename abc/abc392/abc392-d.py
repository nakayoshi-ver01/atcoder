from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
dice=[]
num_of_surface=[]
for _ in range(n):
    c,*surface=map(int,input().split())
    mds=defaultdict(int)
    for i in surface:
        mds[i]+=1
    num_of_surface.append(c)
    dice.append(mds)

ans=0
for i in range(n):
    for j in range(i+1,n):
        all_pattern=num_of_surface[i]*num_of_surface[j]
        i_set=set(dice[i].keys())
        j_set=set(dice[j].keys())
        test=i_set&j_set
        f=0
        for x in test:
            f+=dice[i][x]*dice[j][x]
        ans=max(ans,f/all_pattern)
print(ans)