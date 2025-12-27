from collections import defaultdict,deque
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

skill_tree=defaultdict(set)
state=deque()
bf=[True for _ in range(n+1)]
for i in range(n):
    path=list(map(int,input().split()))
    if path==[0,0]:
        state.append(i+1)
        bf[i+1]=False
    else:
        skill_tree[path[0]].add(i+1)
        skill_tree[path[1]].add(i+1)


while state:
    now=state.popleft()
    for i in skill_tree[now]:
        if bf[i]:
            state.append(i)
            bf[i]=False

print(bf.count(False))