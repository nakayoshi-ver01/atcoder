# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
n,m=map(int,input().split())
# a=list(map(int,input().split()))
s=list(input())
t=list(input())
# grid=[list(input()) for _ in range(h)]
ans=10**9
for i in range(n-m+1):
    temp=0
    for j in range(m):
        temp+=(int(s[i+j])-int(t[j]))%10
    ans=min(ans,temp)
print(ans)