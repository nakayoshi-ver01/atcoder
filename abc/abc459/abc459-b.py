# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
a=list(input().split())
# s=list(input())
# grid=[list(input()) for _ in range(h)]
key=[{'a','b','c'},{'d','e','f'},{'g','h','i'},{'j','k','l'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y','z'}]

for i in range(n):
    for j in range(len(key)):
        if a[i][0] in key[j]:
            print(j+2,end='')
            break

