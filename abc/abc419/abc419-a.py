from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=input()
# grid=[list(input()) for _ in range(h)]
words={
    'red':'SSS',
    'blue':'FFF',
    'green':'MMM'
}

if s in words:
    print(words[s])
else:
    print('Unknown')