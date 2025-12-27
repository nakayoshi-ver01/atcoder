# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,s=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

rui=[0]
revrui=[0]
for i in a:
    rui.append(rui[-1]+i)
for i in reversed(a):
    revrui.append(revrui[-1]+i)

setrui=set(rui)
if s<sum(a):
    for i in rui:
        if i-s in setrui:
            print('Yes')
            break
    else:
        print('No')
else:
    s%=sum(a)
    setrevrui=set(revrui)
    for i in rui:
        if s-i in setrevrui or s+rui[-1]-i in setrevrui:
            print('Yes')
            break
    else:
        print('No')
    