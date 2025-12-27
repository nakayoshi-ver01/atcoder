# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
t=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

for _ in range(t):
    n=int(input())
    s=list(input())
    z_count=0
    o_count=0
    now=''
    combo=0
    z_max_combo=0
    o_max_combo=0
    for i in s:
        if i=='0':
            z_count+=1
        else:
            o_count+=1
        if now!=i:
            if now=='0':
                z_max_combo=max(combo,z_max_combo)
            else:
                o_max_combo=max(combo,o_max_combo)
            now=i
            combo=1
        else:
            combo+=1
    if now=='0':
        z_max_combo=max(combo,z_max_combo)
    else:
        o_max_combo=max(combo,o_max_combo)
    now=i
    combo=1

    print(min((z_count-z_max_combo)*2+o_count,(o_count-o_max_combo)*2+z_count))