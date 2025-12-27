# from collections import defaultdict,deque
# from sortedcontainers import SortedList,SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,d=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())

for i in range(d):
    p=n-1
    while 1:
        if s[p]=='@':
            s[p]='.'
            break
        p-=1
print(''.join(s))