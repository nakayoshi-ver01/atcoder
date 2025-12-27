# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# sys.setrecursionlimit(10**9)
# import math
# import bisect
# import heapq
# n=int(input())
# x,y,z=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

ans=0

for i in range(1,101):
    for j in range(1,101):
        for z in range(2,11):
            if (i-j*z)%(z-1)==0 and (i-j*z)>=0:
                if ans<(i-j*z)//(z-1):
                    ans=max(ans,(i-j*z)//(z-1))
                    print(ans,i,j,z)