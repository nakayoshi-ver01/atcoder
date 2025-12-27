# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
# n,m=map(int,input().split())
a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if a[0]>a[2]:
    print('Yes')
elif a[0]==a[2]:
    if a[1]>a[3]:
        print('Yes')
    else:
        print('No')
else:
    print('No')