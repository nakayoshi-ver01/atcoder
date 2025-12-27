# from collections import defaultdict,deque
# from sortedcontainers import SortedList,SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
a=list(input())

d=a.count('.')
k=min(a.count('@'),m)
print(d+k)