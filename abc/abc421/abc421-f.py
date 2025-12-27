from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
import itertools
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

pattern=6**5
face=defaultdict(int)
for i in a:
    face[i]+=1


once=defaultdict(list)
for i in face:
    once[(i,0)]=[0]
    for k in range(1,6):
        for j in range(k+1):
            once[(i,k)].append(i*j*pow(face[i],j)*pow(6-face[i],k-j)/(6**k))

for i in range(6):
    print(once[(1,i)])

z=list(itertools.combinations_with_replacement(list(face.keys()), 2))


