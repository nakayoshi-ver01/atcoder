from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

state=deque()
for i in a:
    if len(state)<3:
        state.append(i)
    else:
        if state[-1]==state[-2]==state[-3]==i:
            state.pop()
            state.pop()
            state.pop()
        else:
            state.append(i)

print(len(state))