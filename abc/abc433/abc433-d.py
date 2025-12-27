from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

digit_mod=defaultdict(int)

for i in range(1,11):
    for j in a:
        digit_mod[(i,(j*(10**i))%m)]+=1

ans=0

for i in a:
    p=len(str(i))
    ans+=digit_mod[(p,(-i)%m)]
print(ans)