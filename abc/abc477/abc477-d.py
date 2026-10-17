from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,q=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]
# from functools import cmp_to_key, lru_cache

all_cl='a'
fix_color=dict()
unfix_color=dict()
for _ in range(q):
    query=a=list(input().split())
    if query[0]=='1':
        query[1]=int(query[1])-1
        if query[1] in fix_color:
            unfix_color[query[1]]=fix_color[query[1]]
            del fix_color[query[1]]
        elif query[1] in unfix_color:
            fix_color[query[1]]=unfix_color[query[1]]
            del unfix_color[query[1]]
        else:
            fix_color[query[1]]=all_cl
    elif query[0]=='2':
        unfix_color.clear()
        all_cl=query[1]

for i in range(n):
    if i in fix_color:
        print(fix_color[i],end='')
    elif i in unfix_color:
        print(unfix_color[i],end='')
    else:
        print(all_cl,end='')