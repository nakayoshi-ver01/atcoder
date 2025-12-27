# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,r,c=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

fire=[0,0]
human=[r,c]
bonfire=set()
for i in range(n):
    bonfire.add(tuple(fire))
    if s[i]=='N':
        fire[0]+=1
        human[0]+=1
    elif s[i]=='S':
        fire[0]-=1
        human[0]-=1
    elif s[i]=='W':
        fire[1]+=1
        human[1]+=1
    elif s[i]=='E':
        fire[1]-=1
        human[1]-=1
    if tuple(human) in bonfire:
        print(1,end='')
    else:
        print(0,end='')