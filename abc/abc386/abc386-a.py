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
a.sort()
if a.count(a[0])==4:
    print('No')
elif a[0]==a[1] and a[2]==a[3]:
    print('Yes')
elif a[0]==a[1]==a[2]:
    print('Yes')
elif a[3]==a[1]==a[2]:
    print('Yes')
else:
    print('No')