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
s=list(input())
# grid=[list(input()) for _ in range(h)]
left=0
right=0
count=0

if s[left]=='o':
    count+=1

while count>0 and right<n:
    if right<n and s[right]=='o':
        count+=1
    count-=1
    right+=1

if s[0]=='o':
    print(right)
    while left<n and right<n:
        left+=1
        count+=1
        while count>0 and right<n:
            if right<n and s[right]=='o':
                count+=1
            count-=1
            right+=1
        print(right)

    for i in range(left+1,n):
        print(right)
else:
    while left<n and right<n:
        left+=1
        count+=1
        while count>0 and right<n:
            if right<n and s[right]=='o':
                count+=1
            count-=1
            right+=1
        print(right)

    for i in range(left+1,n+1):
        print(right)