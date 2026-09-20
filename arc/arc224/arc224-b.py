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
    root_n=int(pow(n,(1/2)))
    a=root_n
    b=n//root_n
    ans=2*a*b-a-b
    rem=n-a*b
    if rem!=0:
        ans+=(rem-1)+rem
    print(ans)