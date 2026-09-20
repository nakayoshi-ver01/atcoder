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

if n==1:
    if s[0]=='x':
        print(1)
    else:
        print(0)
else:
    ans=0
    for i in range(n):
        if i==0:
            if s[i]=='x' and s[i+1]=='x':
                ans+=1
        elif i==n-1:
            if s[i]=='x' and s[i-1]=='x':
                ans+=1
        else:
            if s[i]=='x' and s[i-1]=='x' and s[i+1]=='x':
                ans+=1
    print(ans)