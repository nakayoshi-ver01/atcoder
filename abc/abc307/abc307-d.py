from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

seq=deque()
parenthese_count=0
for i in s:
    if i=='(':
        parenthese_count+=1
        seq.append(i)
    elif i==')' and parenthese_count>0:
        parenthese_count-=1
        z=seq.pop()
        while z!='(':
            z=seq.pop()
    else:
        seq.append(i)

while seq:
    print(seq.popleft(),end='')