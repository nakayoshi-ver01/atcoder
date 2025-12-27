# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
import bisect
# import heapq
n=int(input())
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

arange=0
while 2**arange<=n:
    arange+=1
ans=0

left=0
right=10**9
center=(left+right)//2
while left+1<right:
    center=(left+right)//2
    if n<2*(center**2):
        right=center
    else:
        left=center
ans+=left


left=0
right=10**9
center=(left+right)//2
while left+1<right:
    center=(left+right)//2
    if n<4*(center**2):
        right=center
    else:
        left=center
ans+=left

print(ans)