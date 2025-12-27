from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
x=list(map(int,input().split()))
p=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

population=defaultdict(int)
x.insert(0,-10**10-1)
x.append(10**9+1)
p.insert(0,0)
p.append(0)
population[-10**10-1]=0

for i in range(1,n+2):
    population[x[i]]=population[x[i-1]]+p[i]

# print(population)

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    l_village=bisect.bisect_left(x,l)-1
    r_village=bisect.bisect_right(x,r)-1
    print(population[x[r_village]]-population[x[l_village]])
    