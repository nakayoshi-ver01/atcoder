# from collections import defaultdict,deque
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

a_cost=0
b_cost=0

a_pos=[]
for i in range(2*n):
    if s[i]=='A':
        a_pos.append(i)

for i in range(n):
    a_cost+=abs(2*i-a_pos[i])
    b_cost+=abs((2*i+1)-a_pos[i])
print(min(a_cost,b_cost))