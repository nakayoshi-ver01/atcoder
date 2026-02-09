# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
q=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]


music=False
volume=0
for _ in range(q):
    query=int(input())
    if query==1:
        volume+=1
    elif query==2:
        volume=max(0,volume-1)
    elif query==3:
        music=not music
    
    if music and volume>=3:
        print('Yes')
    else:
        print('No')
