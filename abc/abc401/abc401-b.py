# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

flg=False
ans=0
for _ in range(n):
    s=input()
    if s=='login':
        flg=True
    elif s=='logout':
        flg=False
    elif s=='private':
        if not flg:
            ans+=1
print(ans)