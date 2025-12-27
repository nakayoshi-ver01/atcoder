# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
# grid=[list(input()) for _ in range(h)]

max_fill=0
for i in range(len(s)):
    for j in range(i+2,len(s)):
        if s[i]=='t' and s[j]=='t':
            exist_t=0
            for k in range(i+1,j):
                if s[k]=='t':
                    exist_t+=1
            max_fill=max(max_fill,exist_t/((j-i)-1))
print(max_fill)