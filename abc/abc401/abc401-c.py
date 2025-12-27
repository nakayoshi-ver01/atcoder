# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
n,k=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

bonacci = [1 for _ in range(k)]
bonacci.append(sum(bonacci))
for i in range(k+1,n+1):
    bonacci.append((2*bonacci[-1]-bonacci[i-k-1])%(10**9))
print(bonacci[n])