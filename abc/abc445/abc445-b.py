# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

words=list()
max_len=0
for _ in range(n):
    word=input()
    max_len=max(max_len,len(word))
    words.append(word)

for i in words:
    k=(max_len-len(i))//2
    print('.'*k+i+'.'*k)
