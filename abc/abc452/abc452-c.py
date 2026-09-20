from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
import sys
sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
rules=[tuple(map(int,input().split())) for _ in range(n)]
m=int(input())
s=[input() for _ in range(m)]
# grid=[list(input()) for _ in range(h)]

words_dict=defaultdict(list)
for i in range(m):
    for j in range(len(s[i])):
        words_dict[(j,s[i][j],len(s[i]))].append(s[i])


for i in range(m):
    if len(s[i]) != n:
        print('No')
    else:
        for j in range(n):
            if not words_dict[(rules[j][1]-1,s[i][j],rules[j][0])]:
                print('No')
                break
        else:
            print('Yes')
        