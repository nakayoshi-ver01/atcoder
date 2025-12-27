# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,c1,c2=map(str,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

for i in range(int(n)):
    if s[i]!=c1:
        s[i]=c2
print(''.join(s))