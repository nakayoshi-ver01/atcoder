# from collections import defaultdict,deque
# from sortedcontainers import SortedList, SortedSet
# import sys
# import math
# import bisect
# import heapq
# n=int(input())
a,b,c=map(int,input().split())
# a=list(map(int,input().split()))
# s=list(input())
# grid=[list(input()) for _ in range(h)]

if a==b==c:
    print('Yes')
else:
    if a==b+c or b==c+a or c==a+b:
        print('Yes')
    else:
        print('No')