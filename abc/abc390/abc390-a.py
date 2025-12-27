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
flg=0
for i in range(4):
    if a[i]!=i+1:
        a[i],a[i+1]=a[i+1],a[i]
        flg=1
        break
else:
    print('No')

if flg:
    if a==[1,2,3,4,5]:
        print('Yes')
    else:
        print('No')