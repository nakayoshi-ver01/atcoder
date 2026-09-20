from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
import bisect
# import heapq
# n=int(input())
n,l,r=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

chars=defaultdict(list)
for i in range(n):
    chars[s[i]].append(i)


ans=0
for i in chars:
    for j in chars[i]:
        l_lim=bisect.bisect_left(chars[i],j+l)
        r_lim=bisect.bisect_right(chars[i],j+r)
        ans+=r_lim-l_lim
print(ans)